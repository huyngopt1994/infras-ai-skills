#!/usr/bin/env bash

set -euo pipefail

CHART_DIR="${1:-.}"
VALUES_FILE="${2:-${CHART_DIR}/values.yaml}"
RELEASE_NAME="${RELEASE_NAME:-skill-helm-check}"
NAMESPACE="${NAMESPACE:-default}"
TMP_RENDERED=""

cleanup() {
  if [[ -n "${TMP_RENDERED}" && -f "${TMP_RENDERED}" ]]; then
    rm -f "${TMP_RENDERED}"
  fi
}

trap cleanup EXIT

run_optional() {
  local name="$1"
  shift

  if command -v "$1" >/dev/null 2>&1; then
    echo "==> ${name}"
    "$@"
  else
    echo "==> ${name} skipped: missing command '$1'"
  fi
}

echo "Validating Helm chart in ${CHART_DIR}"

run_optional "helm lint" helm lint "${CHART_DIR}"

if command -v helm >/dev/null 2>&1; then
  TMP_RENDERED="$(mktemp)"

  echo "==> helm template"
  if [[ -f "${VALUES_FILE}" ]]; then
    helm template "${RELEASE_NAME}" "${CHART_DIR}" --namespace "${NAMESPACE}" --values "${VALUES_FILE}" > "${TMP_RENDERED}"
  else
    echo "values file not found at ${VALUES_FILE}; rendering with chart defaults"
    helm template "${RELEASE_NAME}" "${CHART_DIR}" --namespace "${NAMESPACE}" > "${TMP_RENDERED}"
  fi

  if command -v kubeconform >/dev/null 2>&1; then
    echo "==> kubeconform"
    kubeconform -strict "${TMP_RENDERED}"
  else
    echo "==> kubeconform skipped: missing command 'kubeconform'"
  fi

  if command -v kubectl >/dev/null 2>&1; then
    if kubectl config current-context >/dev/null 2>&1; then
      echo "==> kubectl dry-run=client"
      kubectl apply --dry-run=client --validate=false -f "${TMP_RENDERED}" >/dev/null
    else
      echo "==> kubectl dry-run=client skipped: no usable kube context"
    fi
  else
    echo "==> kubectl dry-run=client skipped: missing command 'kubectl'"
  fi
else
  echo "==> helm template skipped: missing command 'helm'"
fi
