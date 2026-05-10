#!/usr/bin/env bash

set -euo pipefail

NAMESPACE="${1:-}"
POD="${2:-}"
CONTAINER="${3:-}"

if [[ -z "${NAMESPACE}" || -z "${POD}" ]]; then
  echo "Usage: $0 <namespace> <pod> [container]" >&2
  exit 1
fi

if ! command -v kubectl >/dev/null 2>&1; then
  echo "kubectl is required" >&2
  exit 1
fi

DESCRIBE_FILE="describe_pod.txt"
LOG_FILE="log_error.txt"

echo "==> capturing pod description to ${DESCRIBE_FILE}"
kubectl describe pod -n "${NAMESPACE}" "${POD}" > "${DESCRIBE_FILE}"

log_args=(logs -n "${NAMESPACE}" "${POD}" --tail=200)

if [[ -n "${CONTAINER}" ]]; then
  log_args+=(--container "${CONTAINER}")
fi

echo "==> capturing pod logs to ${LOG_FILE}"
if kubectl "${log_args[@]}" --previous > "${LOG_FILE}" 2>/dev/null; then
  :
else
  kubectl "${log_args[@]}" > "${LOG_FILE}"
fi

echo "wrote ${DESCRIBE_FILE}"
echo "wrote ${LOG_FILE}"
