#!/usr/bin/env bash

set -euo pipefail

TARGET_DIR="${1:-.}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

has_terraform=false
has_terragrunt=false

if find "${TARGET_DIR}" -type f -name '*.tf' -print -quit >/dev/null 2>&1; then
  has_terraform=true
fi

if find "${TARGET_DIR}" -type f -name 'terragrunt.hcl' -print -quit >/dev/null 2>&1; then
  has_terragrunt=true
fi

if [[ "${has_terraform}" == "false" && "${has_terragrunt}" == "false" ]]; then
  echo "No IaC files detected under ${TARGET_DIR} (no *.tf or terragrunt.hcl)." >&2
  exit 2
fi

if [[ "${has_terraform}" == "true" ]]; then
  bash "${SCRIPT_DIR}/validate_terraform.sh" "${TARGET_DIR}"
fi

if [[ "${has_terragrunt}" == "true" ]]; then
  bash "${SCRIPT_DIR}/validate_terragrunt.sh" "${TARGET_DIR}"
fi
