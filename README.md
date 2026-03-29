# Infras AI Skills

Terraform and Terragrunt skills packaged for:

- Codex
- Claude Code
- OpenCode

This repo currently ships four skills:

- `terraform`: generate, review, validate, and harden Terraform modules and stacks
- `terragrunt`: scaffold, review, validate, and troubleshoot Terragrunt layouts and dependency wiring
- `github-actions`: create, review, and troubleshoot GitHub Actions workflows, with stronger defaults around least-privilege permissions, fork safety, and reusable workflow patterns
- `github`: standardize repository collaboration files such as `CODEOWNERS`, pull request templates, contributor guidance, and branch protection recommendations

## What Changed

The GitHub-related skills now explicitly push two themes instead of leaving them implicit:

- security-first defaults for Actions and repository governance
- DRY repository patterns so workflow and contributor guidance does not drift across files

In practice that means:

- `github-actions` now calls out minimal `GITHUB_TOKEN` permissions, safer secret handling, immutable action references for higher-risk workflows, OIDC preference, and review checks for unsafe `pull_request_target` usage
- `github-actions` also now steers repeated CI/CD logic toward reusable workflows or composite actions instead of copy-pasting setup, permissions, and cache blocks
- `github` now emphasizes explicit ownership for CI, release, infra, and policy paths, plus stronger merge-control guidance for higher-risk repositories
- `github` also now pushes contributor-doc DRYness by centralizing shared process in `CONTRIBUTING.md` and keeping templates short and purpose-specific

The structure intentionally supports two installation styles:

- direct skill discovery from `terraform-terragrunt-skills-plugin/skills/` for Codex and OpenCode
- plugin-style installation from `terraform-terragrunt-skills-plugin/` for Claude Code and Codex desktop plugin flows

## Repo Layout

```text
.
├── README.md
├── scripts/
└── terraform-terragrunt-skills-plugin/
    ├── .claude-plugin/plugin.json
    ├── .codex-plugin/plugin.json
    └── skills/
        ├── terraform/SKILL.md
        ├── terragrunt/SKILL.md
        ├── github-actions/SKILL.md
        └── github/SKILL.md
```

## Install

### Codex

Direct repo usage:

```bash
mkdir -p ~/.agents/skills
ln -s "$(pwd)/terraform-terragrunt-skills-plugin/skills/terraform" ~/.agents/skills/terraform
ln -s "$(pwd)/terraform-terragrunt-skills-plugin/skills/terragrunt" ~/.agents/skills/terragrunt
ln -s "$(pwd)/terraform-terragrunt-skills-plugin/skills/github-actions" ~/.agents/skills/github-actions
ln -s "$(pwd)/terraform-terragrunt-skills-plugin/skills/github" ~/.agents/skills/github
```

Plugin-style packaging:

```bash
mkdir -p ~/plugins ~/.agents/plugins
ln -s "$(pwd)/terraform-terragrunt-skills-plugin" ~/plugins/terraform-terragrunt-skills
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
      "name": "terraform-terragrunt-skills",
      "source": {
        "source": "local",
        "path": "./plugins/terraform-terragrunt-skills"
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

Clone the repo, then register the local marketplace by linking or copying the root `.claude-plugin/marketplace.json` into your Claude plugin setup. The packaged plugin lives at `terraform-terragrunt-skills-plugin/`.

If you already maintain a Claude marketplace file, merge this plugin entry instead of replacing your existing configuration.

### OpenCode

OpenCode can load Claude-compatible or agent-compatible skill folders. The simplest option is to symlink the repo skills into one of its supported locations:

```bash
REPO_ROOT="$(pwd)"
mkdir -p ~/.config/opencode/skills
ln -s "$REPO_ROOT/terraform-terragrunt-skills-plugin/skills/terraform" ~/.config/opencode/skills/terraform
ln -s "$REPO_ROOT/terraform-terragrunt-skills-plugin/skills/terragrunt" ~/.config/opencode/skills/terragrunt
ln -s "$REPO_ROOT/terraform-terragrunt-skills-plugin/skills/github-actions" ~/.config/opencode/skills/github-actions
ln -s "$REPO_ROOT/terraform-terragrunt-skills-plugin/skills/github" ~/.config/opencode/skills/github
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
ln -s "$HOME/workspace/infras-ai-skills/terraform-terragrunt-skills-plugin/skills/terraform" ~/.config/opencode/skills/terraform
ln -s "$HOME/workspace/infras-ai-skills/terraform-terragrunt-skills-plugin/skills/terragrunt" ~/.config/opencode/skills/terragrunt
ln -s "$HOME/workspace/infras-ai-skills/terraform-terragrunt-skills-plugin/skills/github-actions" ~/.config/opencode/skills/github-actions
ln -s "$HOME/workspace/infras-ai-skills/terraform-terragrunt-skills-plugin/skills/github" ~/.config/opencode/skills/github
```

Or run:

```bash
bash scripts/install-opencode-skills.sh --global
```

3. Verify the install:

```bash
ls ~/.config/opencode/skills/terraform
ls ~/.config/opencode/skills/terragrunt
ls ~/.config/opencode/skills/github-actions
ls ~/.config/opencode/skills/github
```

4. Use the skill name directly in prompts:

- `Use terraform to review this module before I open a PR.`
- `Use terragrunt to scaffold a new environment under infra/live/apac-prod.`

If the device blocks symlinks, copy the skill folders instead:

```bash
mkdir -p ~/.config/opencode/skills
cp -R "$HOME/workspace/infras-ai-skills/terraform-terragrunt-skills-plugin/skills/terraform" ~/.config/opencode/skills/terraform
cp -R "$HOME/workspace/infras-ai-skills/terraform-terragrunt-skills-plugin/skills/terragrunt" ~/.config/opencode/skills/terragrunt
cp -R "$HOME/workspace/infras-ai-skills/terraform-terragrunt-skills-plugin/skills/github-actions" ~/.config/opencode/skills/github-actions
cp -R "$HOME/workspace/infras-ai-skills/terraform-terragrunt-skills-plugin/skills/github" ~/.config/opencode/skills/github
```

For company repos, project-local install is often safer than global install:

```bash
mkdir -p .opencode/skills
cp -R "$HOME/workspace/infras-ai-skills/terraform-terragrunt-skills-plugin/skills/terraform" .opencode/skills/terraform
cp -R "$HOME/workspace/infras-ai-skills/terraform-terragrunt-skills-plugin/skills/terragrunt" .opencode/skills/terragrunt
cp -R "$HOME/workspace/infras-ai-skills/terraform-terragrunt-skills-plugin/skills/github-actions" .opencode/skills/github-actions
cp -R "$HOME/workspace/infras-ai-skills/terraform-terragrunt-skills-plugin/skills/github" .opencode/skills/github
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
- `Use github-actions to review this workflow for unsafe token permissions and flaky execution patterns.`
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
- `Use github-actions to harden ./.github/workflows/release.yml with minimal permissions, concurrency, and safer deploy guards.`
- `Use github-actions to replace repeated job setup across .github/workflows/ with a reusable workflow or composite action.`
- `Use github to standardize this repo with CODEOWNERS, a PR template, and branch protection guidance.`
- `Use github to review whether this repo duplicates process across README, PR templates, and CONTRIBUTING.md, then simplify it.`

When prompting for new infrastructure, include your required labels/tags if your company enforces them:

- `Use terraform to scaffold an AWS module and always include labels project, environment, owner, managed_by, and cost_center.`
- `Use terragrunt to create a live layout and propagate labels project, environment, owner, and cost_center into module inputs.`

## Bundled Helpers

OpenCode, Codex, or Claude can also reuse the bundled scripts and examples:

- installer: `scripts/install-opencode-skills.sh`
- Terraform validator helper: `terraform-terragrunt-skills-plugin/skills/terraform/scripts/validate_terraform.sh`
- Terragrunt validator helper: `terraform-terragrunt-skills-plugin/skills/terragrunt/scripts/validate_terragrunt.sh`
- Terraform example baseline: `terraform-terragrunt-skills-plugin/skills/terraform/examples/minimal-module/`
- Terragrunt example baseline: `terraform-terragrunt-skills-plugin/skills/terragrunt/examples/live-aws/`, including a simple `app -> vpc` dependency example with `mock_outputs` for validation
- GitHub Actions example baseline: `terraform-terragrunt-skills-plugin/skills/github-actions/examples/basic-ci.yml`
- GitHub repository examples: `terraform-terragrunt-skills-plugin/skills/github/examples/`

## GitHub Guidance

If you use the GitHub-related skills, the expected default posture is:

- keep Actions permissions minimal and explicit
- avoid exposing secrets to untrusted pull request execution
- prefer immutable or clearly versioned action references
- use reusable workflows or composite actions when pipelines start repeating themselves
- keep repository ownership clear for CI, release, infrastructure, and policy files
- keep contributor process documented once, then referenced from templates instead of copied everywhere

## Current Scope

This is still a focused skill pack. The current scope is Terraform, Terragrunt, GitHub Actions, and GitHub repository hygiene. Additional platform skills can be added later without changing the packaging model.
