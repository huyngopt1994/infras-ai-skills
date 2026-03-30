# Infras AI Skills

Infrastructure, IaC, and CI/CD skills packaged for:

- Codex
- Claude Code
- OpenCode

This repo is built to capture practical infrastructure engineering guidance from real delivery experience and established industry best practices. The goal is not just to generate files faster, but to raise the quality bar for infrastructure components and delivery pipelines so they are more secure, maintainable, DRY, and production-ready.

The operating model is simple:

- skills should be installable in small, reusable units
- repeated validation should become scripts, not just prose
- each shipped skill should have an example or another concrete reuse path when the domain has a stable baseline

This repo currently ships seven skills:

- `terraform`: generate, review, validate, and harden Terraform modules and stacks
- `terragrunt`: scaffold, review, validate, and troubleshoot Terragrunt layouts and dependency wiring
- `helm`: scaffold, review, validate, and harden Helm charts, values, templates, and Kubernetes workload defaults
- `k8s-doctor`: troubleshoot Kubernetes runtime, Service, endpoint, ingress, and route issues with read-only-first investigation flows
- `github-actions`: create, review, and troubleshoot CI/CD workflows on GitHub Actions, with stronger defaults around least-privilege permissions, fork safety, and reusable workflow patterns
- `github`: standardize repository collaboration files such as `CODEOWNERS`, pull request templates, contributor guidance, and branch protection recommendations that support delivery quality
- `infra-auditor`: perform Infrastructure Review & DevOps Auditor checks that tie IaC, CI/CD, reliability, and application-security controls back to AWS/Azure/GCP well-architected pillars and the OWASP Top 10.

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

- `github-actions` now calls out minimal `GITHUB_TOKEN` permissions, safer secret handling, immutable action references for higher-risk workflows, OIDC preference, and review checks for unsafe `pull_request_target` usage
- `github-actions` also now steers repeated CI/CD logic toward reusable workflows or composite actions instead of copy-pasting setup, permissions, and cache blocks
- `github` now emphasizes explicit ownership for CI, release, infra, and policy paths, plus stronger merge-control guidance for higher-risk repositories
- `github` also now pushes contributor-doc DRYness by centralizing shared process in `CONTRIBUTING.md` and keeping templates short and purpose-specific
- `terraform` and `terragrunt` continue to focus on reusable module contracts, dependency wiring, safer environment structure, and readable input/output boundaries
- `helm` now emphasizes reusable helpers, stable selectors, standard labels, deliberate requests and limits, probes, and safer workload chart defaults
- `k8s-doctor` now emphasizes read-only-first cluster investigation, explicit `-n <namespace>` usage, and bottom-up traffic tracing from Pod to Service to EndpointSlice to HTTPRoute or Ingress
- `infra-auditor` now provides end-to-end infrastructure and DevOps audits that cite AWS/Azure/GCP well-architected pillars, Google SRE practices, and OWASP Top 10 exposure when delivering findings

The repo also now standardizes a lightweight contribution contract: each shipped skill should have a clear trigger, a reusable example when applicable, and a validation path when deterministic local checks are realistic.

Across the full skill pack, the goal is consistent:

- apply best practices from real infrastructure delivery work
- align outputs with common industry safety and maintainability standards
- improve the quality bar for infrastructure components, not just make them syntactically valid

## Purpose

The intended long-term scope of this repo is broader than the current seven skills. It is meant to become a focused infrastructure skills pack covering areas such as:

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

- direct skill discovery from `infras-ai-skills-plugin/skills/` for Codex and OpenCode
- plugin-style installation from `infras-ai-skills-plugin/` for Claude Code and Codex desktop plugin flows

## Repo Layout

```text
.
├── README.md
├── scripts/
└── infras-ai-skills-plugin/
    ├── .claude-plugin/plugin.json
    ├── .codex-plugin/plugin.json
    └── skills/
        ├── terraform/SKILL.md
        ├── terragrunt/SKILL.md
        ├── helm/SKILL.md
        ├── k8s-doctor/SKILL.md
        ├── github-actions/SKILL.md
        ├── github/SKILL.md
        └── infra-auditor/SKILL.md
```

## Install

### Quick Install (recommended)

1. Clone the repo where you keep tooling: `git clone https://github.com/<your-org>/infras-ai-skills.git ~/workspace/infras-ai-skills && cd ~/workspace/infras-ai-skills`.
2. Run the helper script:

   ```bash
   bash scripts/install-opencode-skills.sh --global      # symlinks under ~/.agents/skills and ~/.config/opencode/skills
   # or
   bash scripts/install-opencode-skills.sh --project .   # writes .opencode/skills inside the repo
   ```

3. Enable the plugin/skill pack in Codex, Claude, or OpenCode using their standard local-plugin entry and point it at `infras-ai-skills-plugin/`.

### Manual Symlink Install

```bash
SKILL_ROOT="$(pwd)/infras-ai-skills-plugin/skills"
mkdir -p ~/.agents/skills ~/.config/opencode/skills
for skill in terraform terragrunt helm k8s-doctor github-actions github infra-auditor; do
  ln -sf "$SKILL_ROOT/$skill" ~/.agents/skills/$skill
  ln -sf "$SKILL_ROOT/$skill" ~/.config/opencode/skills/$skill
done
```

Point other agents (Claude, desktop plugins, etc.) at the same directories if they expect different install paths.

### Copy-Only Environments

Some managed laptops block symlinks. After pulling the repo, copy the folders instead:

```bash
SKILL_ROOT="$(pwd)/infras-ai-skills-plugin/skills"
DEST=~/.config/opencode/skills
mkdir -p "$DEST"
for skill in terraform terragrunt helm k8s-doctor github-actions github infra-auditor; do
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

- Mention the skill name in your prompt (`Use terraform …`, `Use infra-auditor …`).
- Always include scope (path, cloud/provider, environment, action like "review" vs. "generate").
- Keep validation steps explicit when you want the skill to run a script or command.

Sample prompts:

- `Use terraform to review ./infra/live/prod for destructive change risk.`
- `Use terragrunt to build a dev/stage/prod layout with a shared root.hcl.`
- `Use helm to refactor ./charts/web with shared helpers and safer defaults.`
- `Use k8s-doctor to trace a 503 from ingress to Pod in namespace payments.`
- `Use github-actions to harden ./.github/workflows/release.yml with minimal permissions and concurrency.`
- `Use github to add CODEOWNERS plus a concise PR template.`
- `Use infra-auditor to audit ./infra and ./.github/workflows for least-privilege IAM, release safety, and OWASP Top 10 exposure before compliance review.`

If your organization mandates specific labels or metadata, add that to the prompt (for example, "include labels project, environment, owner, cost_center" when generating IaC).

## Bundled Helpers

OpenCode, Codex, or Claude can also reuse the bundled scripts and examples:

- installer: `scripts/install-opencode-skills.sh`
- Terraform validator helper: `infras-ai-skills-plugin/skills/terraform/scripts/validate_terraform.sh`
- Terragrunt validator helper: `infras-ai-skills-plugin/skills/terragrunt/scripts/validate_terragrunt.sh`
- Helm validator helper: `infras-ai-skills-plugin/skills/helm/scripts/validate_helm.sh`
- Helm skill: `infras-ai-skills-plugin/skills/helm/SKILL.md`
- Kubernetes debug skill: `infras-ai-skills-plugin/skills/k8s-doctor/SKILL.md`
- Kubernetes debug helper: `infras-ai-skills-plugin/skills/k8s-doctor/scripts/collect_pod_debug.sh`
- Helm example baseline: `infras-ai-skills-plugin/skills/helm/examples/minimal-web-app/`
- Terraform example baseline: `infras-ai-skills-plugin/skills/terraform/examples/minimal-module/`
- Terragrunt example baseline: `infras-ai-skills-plugin/skills/terragrunt/examples/live-aws/`, including a simple `app -> vpc` dependency example with `mock_outputs` for validation
- GitHub Actions example baseline: `infras-ai-skills-plugin/skills/github-actions/examples/basic-ci.yml`
- GitHub repository examples: `infras-ai-skills-plugin/skills/github/examples/`
- Infrastructure audit skill: `infras-ai-skills-plugin/skills/infra-auditor/SKILL.md`

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
- tie infrastructure and application-security findings to OWASP Top 10 categories and cloud well-architected pillars when running infra-auditor reviews

## Current Scope

This is still a focused skill pack. The current shipped scope is Terraform, Terragrunt, Helm, Kubernetes debugging, GitHub Actions, GitHub repository hygiene, and Infrastructure Review & DevOps auditing. The intended direction is broader infrastructure coverage, especially deeper Kubernetes and more general CI/CD skills, without changing the packaging model.

## Future Deliverables

The next expansion area is Kubernetes depth around the existing Helm foundation. The target direction is practical skills that help teams ship and operate workloads safely, not a giant generic Kubernetes encyclopedia.

The likely delivery path is:

- stronger Helm chart generation and validation coverage
- Kubernetes manifest authoring and review skills beyond Helm
- workload debugging and rollout troubleshooting skills
- policy, security, and platform guardrail skills
- packaging patterns that keep examples and validation helpers reusable as the Kubernetes surface grows
- a GKE node pool skill that defaults non-production pools to Spot/preemptible nodes, with clear autoscaler and taint guidance
