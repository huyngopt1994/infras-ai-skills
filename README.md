<div align="center">
  <h1>Infras Kit</h1>
  <h3><em>Turn infrastructure tickets into shippable plans and safe implementations.</em></h3>
</div>

Infrastructure delivery framework and skill pack for:

- Codex
- Claude Code
- OpenCode

Infras Kit focuses on infrastructure work where the repeatable artifacts are a lightweight `spec.md` + `plan.md` + `tasks.md`, plus rollout/rollback, verification evidence, and a Confluence/Jira-ready update.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [What Is Infras Kit?](#what-is-infras-kit)
- [Get Started](#get-started)
- [Default Problem-Solving Flow](#default-problem-solving-flow)
- [Development Phases](#development-phases)
- [Skill Catalog](#skill-catalog)
  - [Operational Notes](#operational-notes)
- [What Changed](#what-changed)
- [Purpose](#purpose)
- [Repo Layout](#repo-layout)
- [Install](#install)
  - [Quick Install (recommended)](#quick-install-recommended)
  - [Manual Symlink Install](#manual-symlink-install)
  - [Copy-Only Environments](#copy-only-environments)
  - [Updating \& Syncing](#updating--syncing)
- [Using The Skills](#using-the-skills)
- [Bundled Helpers](#bundled-helpers)
- [Quality Bar](#quality-bar)
- [Current Scope](#current-scope)
- [Future Deliverables](#future-deliverables)

## What Is Infras Kit?

Infras Kit is a centralized, consistent way to solve infra problems end-to-end:

- intake a ticket
- write a spec and plan with rollout/rollback and verification
- break it into executable tasks
- implement with domain skills (IaC, Helm, GitHub Actions, repo hygiene)
- audit cross-cutting risks before merge/release

## Get Started

1. Install the skills (see [Install](#install)).
2. Create a work item:

```bash
bash infras-kit-plugin/skills/infra-kit/scripts/new-work-item.sh "Reduce NAT Gateway spend" \
  --id "INFRA-1234" \
  --link "https://jira.example.com/browse/INFRA-1234"
```

3. Fill in `docs/infras-kit/work-items/<nnn>-.../ticket.md`, then drive `spec.md` -> `plan.md` -> `tasks.md`.
4. Implement tasks using the domain skill that matches the files you are changing.

## Default Problem-Solving Flow

The canonical flow is documented in `docs/infras-kit/flow.md`.

## Development Phases

Use the skill namespace `infra-kit.*`: everything is under `infra-kit.*`.

1. Intake + artifacts: `infra-kit`
2. Clarify + hypotheses: `infra-kit.thinking`
3. Research (version-dependent): `infra-kit.research`
4. Design (rollout/rollback/ownership): `infra-kit.design`
5. Implement IaC: `infra-kit.iac`
6. Implement charts/manifests: `infra-kit.helm`
7. Debug k8s (read-only-first): `infra-kit.k8s-doctor`
8. Repo + Actions changes: `infra-kit.github`
9. Pre-merge/release audit: `infra-kit.audit`

## Skill Catalog

- `infra-kit`: ticket -> spec -> plan -> tasks -> implementation notes (includes Confluence-ready update template)
- `infra-kit.thinking`: incident triage and decision hygiene when the ticket is ambiguous
- `infra-kit.research`: cited, version-aware research briefs plus a validation plan
- `infra-kit.design`: requirements-first infra design with explicit rollout/rollback and ownership
- `infra-kit.iac`: Terraform + Terragrunt authoring/review/validation
- `infra-kit.helm`: Helm chart authoring/review/validation
- `infra-kit.k8s-doctor`: read-only Kubernetes debugging flows (Pod -> Service -> routing)
- `infra-kit.github`: repo governance and workflow hardening (Actions)
- `infra-kit.audit`: cross-cutting audit (least privilege, release safety, OWASP exposure)

### Operational Notes

- Commits requested through these skills must only include the current change and avoid "AI" or similar phrasing in the message.
- Pull-request descriptions should summarize the latest commit and follow `.github/pull_request_template.md` whenever the target repo has one.
- For non-production GKE node pools, prefer enabling preemptible/Spot capacity to keep the skill's guidance cost-aware by default.
- When reviewing GitHub changes, use `gh` to fetch PR branches and leave context-rich review comments with clear evidence.
- Keep IAM scopes for AWS and GCP resources as least-privilege as possible.
- Always run the repository's formatter or `pre-commit` hooks if they are configured before finalizing work.
- Call out OWASP Top 10 categories when audits surface application-facing or ingress security risks.

## What Changed

The current skills explicitly push a few themes instead of leaving them implicit:

- security-first defaults for infrastructure and delivery workflows
- DRY patterns so infrastructure logic, CI/CD workflows, and contributor guidance do not drift across files
- maintainability and reviewability over fast but brittle generation

In practice that means:

- `infra-kit.github` covers both repo hygiene and Actions hardening: minimal `GITHUB_TOKEN` permissions, fork safety, safer secret handling, and reusable workflows/composite actions to reduce drift
- `infra-kit.github` emphasizes explicit ownership for CI, release, infra, and policy paths, plus stronger merge-control guidance for higher-risk repositories
- `infra-kit.github` pushes contributor-doc DRYness by centralizing shared process in `CONTRIBUTING.md` and keeping templates short and purpose-specific
- `infra-kit.iac` focuses on reusable module contracts, dependency wiring, safer environment structure, and readable input/output boundaries
- `infra-kit.helm` emphasizes reusable helpers, stable selectors, standard labels, deliberate requests and limits, probes, and safer workload chart defaults
- `infra-kit.k8s-doctor` emphasizes read-only-first cluster investigation, explicit `-n <namespace>` usage, and bottom-up traffic tracing from Pod to Service to EndpointSlice to HTTPRoute or Ingress
- `infra-kit.audit` provides end-to-end infrastructure and DevOps audits that cite AWS/Azure/GCP well-architected pillars, Google SRE practices, and OWASP Top 10 exposure when delivering findings

The repo also now standardizes a lightweight contribution contract: each shipped skill should have a clear trigger, a reusable example when applicable, and a validation path when deterministic local checks are realistic.

Across the full skill pack, the goal is consistent:

- apply best practices from real infrastructure delivery work
- align outputs with common industry safety and maintainability standards
- improve the quality bar for infrastructure components, not just make them syntactically valid

## Purpose

The intended long-term scope is broader than the current set of skills. It is meant to become a focused infrastructure kit covering areas such as:

- IaC
- Helm
- Kubernetes
- CI/CD
- delivery and repository hygiene that supports infrastructure quality

The common standard across all of them is the same:

- practical patterns that teams actually use in production
- strong defaults around security and change safety
- DRY, modular structure instead of repetitive configuration
- outputs that are easy to review, evolve, and operate

The structure intentionally supports two installation styles:

- direct skill discovery from `infras-kit-plugin/skills/` for Codex and OpenCode
- plugin-style installation from `infras-kit-plugin/` for Claude Code and Codex desktop plugin flows

## Repo Layout

```text
.
├── README.md
├── docs/
├── scripts/
└── infras-kit-plugin/
    ├── .claude-plugin/plugin.json
    ├── .codex-plugin/plugin.json
    └── skills/
        ├── infra-kit/SKILL.md
        ├── infra-kit.thinking/SKILL.md
        ├── infra-kit.research/SKILL.md
        ├── infra-kit.design/SKILL.md
        ├── infra-kit.iac/SKILL.md
        ├── infra-kit.helm/SKILL.md
        ├── infra-kit.k8s-doctor/SKILL.md
        ├── infra-kit.github/SKILL.md
        └── infra-kit.audit/SKILL.md
```

## Install

### Quick Install (recommended)

1. Clone the repo where you keep tooling: `git clone https://github.com/<your-org>/infras-kit.git ~/workspace/infras-kit && cd ~/workspace/infras-kit`.
2. Run the helper script:

   ```bash
   bash scripts/install-opencode-skills.sh --global      # symlinks under ~/.config/opencode/skills
   # or
   bash scripts/install-opencode-skills.sh --project .   # writes .opencode/skills inside the repo
   ```

3. Enable the plugin/skill pack in Codex, Claude, or OpenCode using their standard local-plugin entry and point it at `infras-kit-plugin/`.

### Manual Symlink Install

```bash
SKILL_ROOT="$(pwd)/infras-kit-plugin/skills"
mkdir -p ~/.agents/skills ~/.config/opencode/skills
for skill in infra-kit infra-kit.thinking infra-kit.research infra-kit.design infra-kit.iac infra-kit.helm infra-kit.k8s-doctor infra-kit.github infra-kit.audit; do
  ln -sf "$SKILL_ROOT/$skill" ~/.agents/skills/$skill
  ln -sf "$SKILL_ROOT/$skill" ~/.config/opencode/skills/$skill
done
```

Point other agents (Claude, desktop plugins, etc.) at the same directories if they expect different install paths.

### Copy-Only Environments

Some managed laptops block symlinks. After pulling the repo, copy the folders instead:

```bash
SKILL_ROOT="$(pwd)/infras-kit-plugin/skills"
DEST=~/.config/opencode/skills
mkdir -p "$DEST"
for skill in infra-kit infra-kit.thinking infra-kit.research infra-kit.design infra-kit.iac infra-kit.helm infra-kit.k8s-doctor infra-kit.github infra-kit.audit; do
  rm -rf "$DEST/$skill"
  cp -R "$SKILL_ROOT/$skill" "$DEST/$skill"
done
```

Use `--project .` with the install script when you want the skills stored inside a specific repository (`.opencode/skills`) rather than globally.

### Updating & Syncing

- If you installed via symlinks, run `git pull` inside your clone and every agent sees the latest skills immediately.
- If you copied the folders, pull first, then rerun the install script (with the same flags) or repeat the copy loop so the destination gets the refreshed files.
- For multi-device setups, treat this repo as the source of truth: pull new commits on each machine, then re-link or copy as needed.

## Using The Skills

- Mention the skill name in your prompt (`Use infra-kit.iac …`, `Use infra-kit.audit …`).
- Always include scope (path, cloud/provider, environment, action like "review" vs. "generate").
- Keep validation steps explicit when you want the skill to run a script or command.

Sample prompts:

- `Use infra-kit.iac to review ./infra/live/prod for destructive change risk.`
- `Use infra-kit.iac to design a dev/stage/prod layout with a shared root.hcl.`
- `Use infra-kit.helm to refactor ./charts/web with shared helpers and safer defaults.`
- `Use infra-kit.k8s-doctor to trace a 503 from ingress to Pod in namespace payments.`
- `Use infra-kit.github to harden ./.github/workflows/release.yml with minimal permissions and concurrency.`
- `Use infra-kit.github to add CODEOWNERS plus a concise PR template.`
- `Use infra-kit.audit to audit ./infra and ./.github/workflows for least-privilege IAM, release safety, and OWASP Top 10 exposure before compliance review.`
- `Use infra-kit to turn this Jira ticket into spec/plan/tasks under docs/infras-kit/work-items/.`

If your organization mandates specific labels or metadata, add that to the prompt (for example, "include labels project, environment, owner, cost_center" when generating IaC).

## Bundled Helpers

- installer: `scripts/install-opencode-skills.sh`
- work-item scaffold: `infras-kit-plugin/skills/infra-kit/scripts/new-work-item.sh`
- IaC validator helper: `infras-kit-plugin/skills/infra-kit.iac/scripts/validate_iac.sh`
- Helm validator helper: `infras-kit-plugin/skills/infra-kit.helm/scripts/validate_helm.sh`
- Helm skill: `infras-kit-plugin/skills/infra-kit.helm/SKILL.md`
- Kubernetes debug skill: `infras-kit-plugin/skills/infra-kit.k8s-doctor/SKILL.md`
- Kubernetes debug helper: `infras-kit-plugin/skills/infra-kit.k8s-doctor/scripts/collect_pod_debug.sh`
- Helm example baseline: `infras-kit-plugin/skills/infra-kit.helm/examples/minimal-web-app/`
- GitHub Actions example baseline: `infras-kit-plugin/skills/infra-kit.github/examples/github-actions/basic-ci.yml`
- GitHub repository examples: `infras-kit-plugin/skills/infra-kit.github/examples/`
- Infrastructure audit skill: `infras-kit-plugin/skills/infra-kit.audit/SKILL.md`

See `CONTRIBUTING.md` for the minimum bar for adding or evolving skills in this repo.

## Quality Bar

If you use these skills, the expected default posture is:

- keep infrastructure and delivery contracts explicit
- keep Actions permissions minimal and explicit
- avoid exposing secrets to untrusted pull request execution
- prefer immutable or clearly versioned action references
- use reusable workflows or composite actions when pipelines start repeating themselves
- keep IaC inputs, outputs, and dependencies readable at the module boundary
- keep Helm charts reviewable, with stable selectors, standard labels, and deliberate workload defaults
- keep Kubernetes troubleshooting read-only first, explicit about namespace scope, and evidence-driven from Pod to route
- keep repository ownership clear for CI, release, infrastructure, and policy files
- keep contributor process documented once, then referenced from templates instead of copied everywhere
- tie infrastructure and application-security findings to OWASP Top 10 categories and cloud well-architected pillars when running infra-kit.audit reviews

## Current Scope

This is still a focused kit. The current shipped scope is IaC (Terraform+Terragrunt), Helm, Kubernetes debugging, GitHub repo + Actions, and Infrastructure Review & DevOps auditing. The intended direction is broader infrastructure coverage, especially deeper Kubernetes and more general CI/CD skills, without changing the packaging model.

## Future Deliverables

The next expansion area is Kubernetes depth around the existing Helm foundation. The target direction is practical skills that help teams ship and operate workloads safely, not a giant generic Kubernetes encyclopedia.

The likely delivery path is:

- stronger Helm chart generation and validation coverage
- Kubernetes manifest authoring and review skills beyond Helm
- workload debugging and rollout troubleshooting skills
- policy, security, and platform guardrail skills
- packaging patterns that keep examples and validation helpers reusable as the Kubernetes surface grows
- a GKE node pool skill that defaults non-production pools to Spot/preemptible nodes, with clear autoscaler and taint guidance
