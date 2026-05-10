<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<br />
<div align="center">
  <a href="#readme-top">
    <img src="images/logo.jpg" alt="Infras Kit logo" width="96" height="96">
  </a>

  <h1 align="center">Infras Kit</h1>

  <p align="center">
    Turn infrastructure tickets into shippable plans and safe implementations.
    <br />
    <a href="docs/infras-kit/flow.md"><strong>Explore the flow docs »</strong></a>
    <br />
    <br />
    <a href="#install">Install</a>
    ·
    <a href="#usage">Usage</a>
    ·
    <a href="CONTRIBUTING.md">Contributing</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#install">Install</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#skill-catalog">Skill Catalog</a></li>
    <li><a href="#repo-layout">Repo Layout</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Infras Kit screenshot](images/screenshot.jpg)](docs/infras-kit/flow.md)

Infras Kit is a lightweight infrastructure delivery framework and skill pack for agents like Codex, Claude Code, and OpenCode.

It standardizes repeatable artifacts (`ticket.md`, `spec.md`, `plan.md`, `tasks.md`) and pushes safe delivery defaults:

- explicit rollout and rollback steps
- verification evidence and “done” checks
- security-first repo and CI/CD guardrails

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- Markdown-first workflow under `docs/`
- Shell scripts for scaffolding/validation under `scripts/` and `infras-kit-plugin/skills/*/scripts/`
- Skill packs under `infras-kit-plugin/skills/`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- `git`
- `bash`

### Install

#### Quick install (recommended)

```bash
bash scripts/install-opencode-skills.sh --global      # symlinks under ~/.config/opencode/skills
# or
bash scripts/install-opencode-skills.sh --project .   # writes .opencode/skills inside this repo
```

Enable the plugin/skill pack in Codex, Claude, or OpenCode using their standard local-plugin entry and point it at `infras-kit-plugin/`.

#### Manual symlink install

```bash
SKILL_ROOT="$(pwd)/infras-kit-plugin/skills"
mkdir -p ~/.agents/skills ~/.config/opencode/skills
for skill in infra-kit.workflow infra-kit.workflow.thinking infra-kit.workflow.research infra-kit.workflow.design infra-kit.domain.iac infra-kit.domain.helm infra-kit.domain.k8s-doctor infra-kit.domain.github infra-kit.workflow.audit; do
  ln -sf "$SKILL_ROOT/$skill" ~/.agents/skills/$skill
  ln -sf "$SKILL_ROOT/$skill" ~/.config/opencode/skills/$skill
done
```

#### Copy-only environments

Some managed laptops block symlinks. After pulling the repo, copy the folders instead:

```bash
SKILL_ROOT="$(pwd)/infras-kit-plugin/skills"
DEST=~/.config/opencode/skills
mkdir -p "$DEST"
for skill in infra-kit.workflow infra-kit.workflow.thinking infra-kit.workflow.research infra-kit.workflow.design infra-kit.domain.iac infra-kit.domain.helm infra-kit.domain.k8s-doctor infra-kit.domain.github infra-kit.workflow.audit; do
  rm -rf "$DEST/$skill"
  cp -R "$SKILL_ROOT/$skill" "$DEST/$skill"
done
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE -->
## Usage

1. Scaffold a work item:

```bash
bash infras-kit-plugin/skills/infra-kit.workflow/scripts/new-work-item.sh "Reduce NAT Gateway spend" \
  --id "INFRA-1234" \
  --link "https://jira.example.com/browse/INFRA-1234"
```

2. Fill in `docs/infras-kit/work-items/<nnn>-.../ticket.md`, then drive `spec.md` -> `plan.md` -> `tasks.md`.
3. Implement tasks using the domain skill that matches the files you are changing.

Sample prompts:

```text
Use infra-kit.domain.iac to review ./infra/live/prod for destructive change risk.
Use infra-kit.domain.helm to refactor ./charts/web with shared helpers and safer defaults.
Use infra-kit.domain.k8s-doctor to trace a 503 from ingress to Pod in namespace payments.
Use infra-kit.domain.github to harden ./.github/workflows/release.yml with minimal permissions.
Use infra-kit.workflow.audit to audit ./infra and ./.github/workflows for least-privilege and release safety.
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SKILL CATALOG -->
## Skill Catalog

- `infra-kit.workflow`: ticket -> spec -> plan -> tasks -> implementation notes (includes Confluence-ready update template)
- `infra-kit.workflow.thinking`: structured problem solving and decision hygiene
- `infra-kit.workflow.research`: version-aware, source-backed research briefs with a validation plan
- `infra-kit.workflow.design`: requirements-first infrastructure design with rollout/rollback and ownership
- `infra-kit.domain.iac`: Terraform + Terragrunt authoring/review/validation
- `infra-kit.domain.helm`: Helm chart authoring/review/validation
- `infra-kit.domain.k8s-doctor`: read-only-first Kubernetes debugging (Pod -> Service -> routing)
- `infra-kit.domain.github`: repo governance and workflow hardening (Actions, CODEOWNERS, templates)
- `infra-kit.workflow.audit`: cross-cutting audit (least privilege, release safety, OWASP exposure)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- REPO LAYOUT -->
## Repo Layout

```text
.
├── README.md
├── images/
├── docs/
├── scripts/
└── infras-kit-plugin/
    ├── .claude-plugin/plugin.json
    ├── .codex-plugin/plugin.json
    └── skills/
        ├── infra-kit.workflow/SKILL.md
        ├── infra-kit.workflow.thinking/SKILL.md
        ├── infra-kit.workflow.research/SKILL.md
        ├── infra-kit.workflow.design/SKILL.md
        ├── infra-kit.domain.iac/SKILL.md
        ├── infra-kit.domain.helm/SKILL.md
        ├── infra-kit.domain.k8s-doctor/SKILL.md
        ├── infra-kit.domain.github/SKILL.md
        └── infra-kit.workflow.audit/SKILL.md
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

This repository currently does not include a `LICENSE` file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
