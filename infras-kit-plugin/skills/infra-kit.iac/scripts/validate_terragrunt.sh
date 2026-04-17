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

echo "Validating Terragrunt in ${TARGET_DIR}"

run_optional "terragrunt hcl fmt" terragrunt hcl fmt --check --working-dir "${TARGET_DIR}"
run_optional "terragrunt init" terragrunt run --all init --working-dir "${TARGET_DIR}" --backend=false
run_optional "terragrunt validate" terragrunt run --all validate --working-dir "${TARGET_DIR}"
run_optional "tflint" tflint --chdir="${TARGET_DIR}"
