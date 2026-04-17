#!/usr/bin/env bash

set -euo pipefail

title="${1:-}"
shift || true

if [[ -z "${title}" ]]; then
  echo "Usage: new-work-item.sh \"<short title>\" [--id ID] [--link URL]" >&2
  exit 2
fi

ticket_id=""
ticket_link=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --id)
      ticket_id="${2:-}"
      shift 2
      ;;
    --link)
      ticket_link="${2:-}"
      shift 2
      ;;
    --help|-h)
      echo "Usage: new-work-item.sh \"<short title>\" [--id ID] [--link URL]" >&2
      exit 0
      ;;
    *)
      echo "Unknown arg: $1" >&2
      exit 2
      ;;
  esac
done

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/../../../.." && pwd)"

templates_dir="${repo_root}/infras-kit-plugin/skills/infra-kit/templates"
base_dir="${repo_root}/docs/infras-kit/work-items"

mkdir -p "${base_dir}"

slug="$(echo "${title}" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-' | sed 's/^-//; s/-$//')"
if [[ -z "${slug}" ]]; then
  slug="work-item"
fi

next_num="001"
if ls "${base_dir}"/* >/dev/null 2>&1; then
  last="$(ls -1 "${base_dir}" 2>/dev/null | sed -n 's/^\([0-9]\+\)-.*/\1/p' | sort -n | tail -n 1 || true)"
  if [[ -n "${last}" ]]; then
    next_num="$(printf "%03d" $((10#${last} + 1)))"
  fi
fi

dir_name="${next_num}-${slug}"
work_dir="${base_dir}/${dir_name}"

if [[ -e "${work_dir}" ]]; then
  echo "Already exists: ${work_dir}" >&2
  exit 1
fi

mkdir -p "${work_dir}"

copy_template() {
  local src="$1"
  local dst="$2"
  cp "${templates_dir}/${src}" "${work_dir}/${dst}"
}

copy_template ticket.md ticket.md
copy_template spec.md spec.md
copy_template plan.md plan.md
copy_template tasks.md tasks.md
copy_template implementation-notes.md implementation-notes.md
copy_template confluence.md confluence.md

if [[ -n "${ticket_id}" || -n "${ticket_link}" ]]; then
  # Minimal, portable substitution without relying on GNU sed -i.
  tmp_file="${work_dir}/.ticket.tmp"
  awk -v id="${ticket_id}" -v link="${ticket_link}" '
    BEGIN { }
    {
      gsub("<ID>", id);
      gsub("<URL>", link);
      print
    }
  ' "${work_dir}/ticket.md" > "${tmp_file}"
  mv "${tmp_file}" "${work_dir}/ticket.md"
fi

echo "Created work item: ${work_dir}"
