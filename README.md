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

This repo currently ships six skills:

- `terraform`: generate, review, validate, and harden Terraform modules and stacks
- `terragrunt`: scaffold, review, validate, and troubleshoot Terragrunt layouts and dependency wiring
- `helm`: scaffold, review, validate, and harden Helm charts, values, templates, and Kubernetes workload defaults
- `k8s-doctor`: troubleshoot Kubernetes runtime, Service, endpoint, ingress, and route issues with read-only-first investigation flows
- `github-actions`: create, review, and troubleshoot CI/CD workflows on GitHub Actions, with stronger defaults around least-privilege permissions, fork safety, and reusable workflow patterns
- `github`: standardize repository collaboration files such as `CODEOWNERS`, pull request templates, contributor guidance, and branch protection recommendations that support delivery quality

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

The repo also now standardizes a lightweight contribution contract: each shipped skill should have a clear trigger, a reusable example when applicable, and a validation path when deterministic local checks are realistic.

Across the full skill pack, the goal is consistent:

- apply best practices from real infrastructure delivery work
- align outputs with common industry safety and maintainability standards
- improve the quality bar for infrastructure components, not just make them syntactically valid

## Purpose

The intended long-term scope of this repo is broader than the current six skills. It is meant to become a focused infrastructure skills pack covering areas such as:

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
        └── github/SKILL.md
```

## Install

### Codex

Direct repo usage:

```bash
mkdir -p ~/.agents/skills
ln -s "$(pwd)/infras-ai-skills-plugin/skills/terraform" ~/.agents/skills/terraform
ln -s "$(pwd)/infras-ai-skills-plugin/skills/terragrunt" ~/.agents/skills/terragrunt
ln -s "$(pwd)/infras-ai-skills-plugin/skills/helm" ~/.agents/skills/helm
ln -s "$(pwd)/infras-ai-skills-plugin/skills/k8s-doctor" ~/.agents/skills/k8s-doctor
ln -s "$(pwd)/infras-ai-skills-plugin/skills/github-actions" ~/.agents/skills/github-actions
ln -s "$(pwd)/infras-ai-skills-plugin/skills/github" ~/.agents/skills/github
```

Plugin-style packaging:

```bash
mkdir -p ~/plugins ~/.agents/plugins
ln -s "$(pwd)/infras-ai-skills-plugin" ~/plugins/infras-ai-skills
```

Then add or merge this entry into `~/.agents/plugins/marketplace.json`:

```json
{
  "name": "local-plugins",
  "interface": {
    "displayName": "Local Plugins"
  },
  "plugins": [
    {
      "name": "infras-ai-skills",
      "source": {
        "source": "local",
        "path": "./plugins/infras-ai-skills"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

### Claude Code

Clone the repo, then register the local marketplace by linking or copying the root `.claude-plugin/marketplace.json` into your Claude plugin setup. The packaged plugin lives at `infras-ai-skills-plugin/`.

If you already maintain a Claude marketplace file, merge this plugin entry instead of replacing your existing configuration.

### OpenCode

OpenCode can load Claude-compatible or agent-compatible skill folders. The simplest option is to symlink the repo skills into one of its supported locations:

```bash
REPO_ROOT="$(pwd)"
mkdir -p ~/.config/opencode/skills
ln -s "$REPO_ROOT/infras-ai-skills-plugin/skills/terraform" ~/.config/opencode/skills/terraform
ln -s "$REPO_ROOT/infras-ai-skills-plugin/skills/terragrunt" ~/.config/opencode/skills/terragrunt
ln -s "$REPO_ROOT/infras-ai-skills-plugin/skills/helm" ~/.config/opencode/skills/helm
ln -s "$REPO_ROOT/infras-ai-skills-plugin/skills/k8s-doctor" ~/.config/opencode/skills/k8s-doctor
ln -s "$REPO_ROOT/infras-ai-skills-plugin/skills/github-actions" ~/.config/opencode/skills/github-actions
ln -s "$REPO_ROOT/infras-ai-skills-plugin/skills/github" ~/.config/opencode/skills/github
```

You can also place them under project-local `.opencode/skills/`, `.claude/skills/`, or any equivalent agent skill directory your tool supports.

Or use the installer script:

```bash
bash scripts/install-opencode-skills.sh --global
```

### OpenCode On Another Machine

If you use OpenCode on multiple laptops or a managed workstation, keep this repo as the source of truth and install from it on each device.

Recommended setup:

1. Clone the repo on that machine:

```bash
git clone https://github.com/<your-org>/infras-ai-skills.git ~/workspace/infras-ai-skills
cd ~/workspace/infras-ai-skills
```

2. Link the skills into OpenCode's global skill directory:

```bash
mkdir -p ~/.config/opencode/skills
ln -s "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/terraform" ~/.config/opencode/skills/terraform
ln -s "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/terragrunt" ~/.config/opencode/skills/terragrunt
ln -s "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/helm" ~/.config/opencode/skills/helm
ln -s "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/k8s-doctor" ~/.config/opencode/skills/k8s-doctor
ln -s "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/github-actions" ~/.config/opencode/skills/github-actions
ln -s "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/github" ~/.config/opencode/skills/github
```

Or run:

```bash
bash scripts/install-opencode-skills.sh --global
```

3. Verify the install:

```bash
ls ~/.config/opencode/skills/terraform
ls ~/.config/opencode/skills/terragrunt
ls ~/.config/opencode/skills/helm
ls ~/.config/opencode/skills/k8s-doctor
ls ~/.config/opencode/skills/github-actions
ls ~/.config/opencode/skills/github
```

4. Use the skill name directly in prompts:

- `Use terraform to review this module before I open a PR.`
- `Use terragrunt to scaffold a new environment under infra/live/apac-prod.`
- `Use helm to review this chart for labels, probes, and request/limit defaults.`
- `Use k8s-doctor to trace why requests reach the ingress but not the backend Pod in namespace payments.`

If the device blocks symlinks, copy the skill folders instead:

```bash
mkdir -p ~/.config/opencode/skills
cp -R "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/terraform" ~/.config/opencode/skills/terraform
cp -R "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/terragrunt" ~/.config/opencode/skills/terragrunt
cp -R "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/helm" ~/.config/opencode/skills/helm
cp -R "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/k8s-doctor" ~/.config/opencode/skills/k8s-doctor
cp -R "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/github-actions" ~/.config/opencode/skills/github-actions
cp -R "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/github" ~/.config/opencode/skills/github
```

For company repos, project-local install is often safer than global install:

```bash
mkdir -p .opencode/skills
cp -R "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/terraform" .opencode/skills/terraform
cp -R "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/terragrunt" .opencode/skills/terragrunt
cp -R "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/helm" .opencode/skills/helm
cp -R "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/k8s-doctor" .opencode/skills/k8s-doctor
cp -R "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/github-actions" .opencode/skills/github-actions
cp -R "$HOME/workspace/infras-ai-skills/infras-ai-skills-plugin/skills/github" .opencode/skills/github
```

Installer version:

```bash
bash "$HOME/workspace/infras-ai-skills/scripts/install-opencode-skills.sh" --project .
```

That keeps the exact skill version with the repository instead of depending on one workstation's global config.

### Syncing Across Devices

Update each cloned copy with:

```bash
cd ~/workspace/infras-ai-skills
git pull
```

If you used symlinks, OpenCode will see the latest changes immediately after pulling. If you copied the folders, copy them again after updating.

## How To Use

Example prompts:

- `Use terraform to scaffold a reusable AWS VPC module with variables, outputs, and validation guidance.`
- `Review this Terraform directory with terraform and list only high-risk findings.`
- `Use terragrunt to create a dev/staging/prod layout with a shared root.hcl and per-environment inputs.`
- `Validate this Terragrunt stack and explain the broken dependency wiring.`
- `Use helm to scaffold a reusable chart for a web app with ingress, probes, and resource sizing values.`
- `Use helm to review this chart for selector stability, labels, and Kubernetes-safe defaults.`
- `Use k8s-doctor to trace a 503 from the Pod through Service, EndpointSlice, and HTTPRoute in namespace payments.`
- `Use k8s-doctor to investigate whether NetworkPolicy or ResourceQuota is why this workload never becomes Ready.`
- `Use github-actions to review this CI workflow for unsafe token permissions and flaky execution patterns.`
- `Use github to add CODEOWNERS and a pull request template for this repository.`
- `Use github-actions to refactor duplicated CI workflows into a reusable workflow and tighten secret handling.`
- `Use github to clean up duplicated contributor instructions and move the shared process into CONTRIBUTING.md.`

## Practical Usage Notes

For OpenCode, the most reliable pattern is:

1. Install the skill globally or per-project.
2. Mention the skill by name in the prompt.
3. Be explicit about scope:
   - target path
   - provider or cloud
   - environments
   - whether you want generation, review, or debugging

Better prompts:

- `Use terraform to refactor ./infra/modules/vpc into a reusable module with typed variables and safer defaults.`
- `Use terraform to review ./infra/live/prod for security and destructive-change risk.`
- `Use terragrunt to design a root.hcl plus dev/staging/prod layout for AWS accounts split by environment.`
- `Use terragrunt to debug why ./infra/live/prod/app cannot read dependency outputs from ./infra/live/prod/vpc.`
- `Use terragrunt to wire an app unit to a vpc unit with dependency blocks and validate-safe mock outputs.`
- `Use helm to review ./charts/api for upgrade risk, helper reuse, label consistency, and safe request/limit defaults.`
- `Use helm to refactor ./charts/web so shared labels and names come from _helpers.tpl instead of copy-pasted templates.`
- `Use k8s-doctor to inspect why ./payments is healthy at the Pod level but the Service still has no endpoints in namespace payments.`
- `Use k8s-doctor to trace traffic bottom-up from Pod to Service to Ingress and ask before any exec or port-forward step.`
- `Use github-actions to harden ./.github/workflows/release.yml with minimal permissions, concurrency, and safer deploy guards.`
- `Use github-actions to replace repeated job setup across .github/workflows/ with a reusable workflow or composite action.`
- `Use github to standardize this repo with CODEOWNERS, a PR template, and branch protection guidance.`
- `Use github to review whether this repo duplicates process across README, PR templates, and CONTRIBUTING.md, then simplify it.`

When prompting for new infrastructure, include your required labels/tags if your company enforces them:

- `Use terraform to scaffold an AWS module and always include labels project, environment, owner, managed_by, and cost_center.`
- `Use terragrunt to create a live layout and propagate labels project, environment, owner, and cost_center into module inputs.`
- `Use helm to add app.kubernetes.io labels plus explicit CPU and memory requests and limits for each workload container.`
- `Use k8s-doctor with read-only commands first and keep every namespaced check explicit with -n payments.`

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

## Current Scope

This is still a focused skill pack. The current shipped scope is Terraform, Terragrunt, Helm, Kubernetes debugging, GitHub Actions, and GitHub repository hygiene. The intended direction is broader infrastructure coverage, especially deeper Kubernetes and more general CI/CD skills, without changing the packaging model.

## Future Deliverables

The next expansion area is Kubernetes depth around the existing Helm foundation. The target direction is practical skills that help teams ship and operate workloads safely, not a giant generic Kubernetes encyclopedia.

The likely delivery path is:

- stronger Helm chart generation and validation coverage
- Kubernetes manifest authoring and review skills beyond Helm
- workload debugging and rollout troubleshooting skills
- policy, security, and platform guardrail skills
- packaging patterns that keep examples and validation helpers reusable as the Kubernetes surface grows
