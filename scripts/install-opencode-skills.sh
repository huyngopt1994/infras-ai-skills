#!/usr/bin/env bash

set -euo pipefail

MODE="link"
TARGET_DIR="${HOME}/.config/opencode/skills"

usage() {
  cat <<'EOF'
Usage:
  scripts/install-opencode-skills.sh [--copy|--link] [--global|--project DIR]

Options:
  --link         Symlink skills into the target directory (default)
  --copy         Copy skills into the target directory
  --global       Install into ~/.config/opencode/skills (default)
  --project DIR  Install into DIR/.opencode/skills
  --help         Show this help
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --copy)
      MODE="copy"
      shift
      ;;
    --link)
      MODE="link"
      shift
      ;;
    --global)
      TARGET_DIR="${HOME}/.config/opencode/skills"
      shift
      ;;
    --project)
      [[ $# -ge 2 ]] || {
        echo "Missing project directory for --project" >&2
        exit 1
      }
      TARGET_DIR="$2/.opencode/skills"
      shift 2
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
SOURCE_DIR="${REPO_ROOT}/terraform-terragrunt-skills-plugin/skills"

mkdir -p "${TARGET_DIR}"

install_skill() {
  local skill_name="$1"
  local src="${SOURCE_DIR}/${skill_name}"
  local dest="${TARGET_DIR}/${skill_name}"

  rm -rf "${dest}"

  if [[ "${MODE}" == "link" ]]; then
    ln -s "${src}" "${dest}"
    echo "linked ${skill_name} -> ${dest}"
  else
    cp -R "${src}" "${dest}"
    echo "copied ${skill_name} -> ${dest}"
  fi
}

install_skill "terraform"
install_skill "terragrunt"
install_skill "github-actions"
install_skill "github"

echo
echo "Install complete: ${TARGET_DIR}"
