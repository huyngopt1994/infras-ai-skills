#!/usr/bin/env bash

set -euo pipefail

TARGET_DIR="${1:-.}"

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

echo "Validating Terraform in ${TARGET_DIR}"

run_optional "terraform fmt" terraform -chdir="${TARGET_DIR}" fmt -recursive
run_optional "terraform init" terraform -chdir="${TARGET_DIR}" init -backend=false
run_optional "terraform validate" terraform -chdir="${TARGET_DIR}" validate
run_optional "tflint" tflint --chdir="${TARGET_DIR}"
run_optional "checkov" checkov -d "${TARGET_DIR}"
