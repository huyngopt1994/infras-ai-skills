# AI Platform Skills

Terraform and Terragrunt skills packaged for:

- Codex
- Claude Code
- OpenCode

This repo starts with two infrastructure skills:

- `terraform`: generate, review, validate, and harden Terraform modules and stacks
- `terragrunt`: scaffold, review, validate, and troubleshoot Terragrunt layouts and dependency wiring

The structure intentionally supports two installation styles:

- direct skill discovery from `.agents/skills/` for Codex and OpenCode
- plugin-style installation from `terraform-terragrunt-skills-plugin/` for Claude Code and Codex desktop plugin flows

## Repo Layout

```text
.
├── .agents/skills/
│   ├── terraform/SKILL.md
│   └── terragrunt/SKILL.md
├── .claude-plugin/marketplace.json
└── terraform-terragrunt-skills-plugin/
    ├── .claude-plugin/plugin.json
    ├── .codex-plugin/plugin.json
    └── skills/
        ├── terraform/SKILL.md
        └── terragrunt/SKILL.md
```

## Install

### Codex

Direct repo usage:

```bash
mkdir -p ~/.agents/skills
ln -s "$(pwd)/.agents/skills/terraform" ~/.agents/skills/terraform
ln -s "$(pwd)/.agents/skills/terragrunt" ~/.agents/skills/terragrunt
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
mkdir -p ~/.config/opencode/skills
ln -s "$(pwd)/.agents/skills/terraform" ~/.config/opencode/skills/terraform
ln -s "$(pwd)/.agents/skills/terragrunt" ~/.config/opencode/skills/terragrunt
```

You can also place them under project-local `.opencode/skills/`, `.claude/skills/`, or `.agents/skills/`.

Or use the installer script:

```bash
bash scripts/install-opencode-skills.sh --global
```

### OpenCode On Another Company Device

If you use OpenCode on multiple laptops or on a company-managed machine, keep this repo as the source of truth and install from it on each device.

Recommended setup:

1. Clone the repo on that machine:

```bash
git clone https://github.com/huyngo/ai-platform-skills.git ~/workspace/ai-platform-skills
cd ~/workspace/ai-platform-skills
```

2. Link the skills into OpenCode's global skill directory:

```bash
mkdir -p ~/.config/opencode/skills
ln -s ~/workspace/ai-platform-skills/.agents/skills/terraform ~/.config/opencode/skills/terraform
ln -s ~/workspace/ai-platform-skills/.agents/skills/terragrunt ~/.config/opencode/skills/terragrunt
```

Or run:

```bash
bash scripts/install-opencode-skills.sh --global
```

3. Verify the install:

```bash
ls ~/.config/opencode/skills/terraform
ls ~/.config/opencode/skills/terragrunt
```

4. Use the skill name directly in prompts:

- `Use terraform to review this module before I open a PR.`
- `Use terragrunt to scaffold a new environment under infra/live/apac-prod.`

If the device blocks symlinks, copy the skill folders instead:

```bash
mkdir -p ~/.config/opencode/skills
cp -R ~/workspace/ai-platform-skills/.agents/skills/terraform ~/.config/opencode/skills/terraform
cp -R ~/workspace/ai-platform-skills/.agents/skills/terragrunt ~/.config/opencode/skills/terragrunt
```

For company repos, project-local install is often safer than global install:

```bash
mkdir -p .opencode/skills
cp -R ~/workspace/ai-platform-skills/.agents/skills/terraform .opencode/skills/terraform
cp -R ~/workspace/ai-platform-skills/.agents/skills/terragrunt .opencode/skills/terragrunt
```

Installer version:

```bash
bash ~/workspace/ai-platform-skills/scripts/install-opencode-skills.sh --project .
```

That keeps the exact skill version with the repository instead of depending on one workstation's global config.

### Syncing Across Devices

Update each cloned copy with:

```bash
cd ~/workspace/ai-platform-skills
git pull
```

If you used symlinks, OpenCode will see the latest changes immediately after pulling. If you copied the folders, copy them again after updating.

## How To Use

Example prompts:

- `Use terraform to scaffold a reusable AWS VPC module with variables, outputs, and validation guidance.`
- `Review this Terraform directory with terraform and list only high-risk findings.`
- `Use terragrunt to create a dev/staging/prod layout with a shared root.hcl and per-environment inputs.`
- `Validate this Terragrunt stack and explain the broken dependency wiring.`

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

When prompting for new infrastructure, include your required labels/tags if your company enforces them:

- `Use terraform to scaffold an AWS module and always include labels project, environment, owner, managed_by, and cost_center.`
- `Use terragrunt to create a live layout and propagate labels project, environment, owner, and cost_center into module inputs.`

## Bundled Helpers

OpenCode, Codex, or Claude can also reuse the bundled scripts and examples:

- installer: `scripts/install-opencode-skills.sh`
- Terraform validator helper: `.agents/skills/terraform/scripts/validate_terraform.sh`
- Terragrunt validator helper: `.agents/skills/terragrunt/scripts/validate_terragrunt.sh`
- Terraform example baseline: `.agents/skills/terraform/examples/minimal-module/`
- Terragrunt example baseline: `.agents/skills/terragrunt/examples/live-aws/`

## Current Scope

This is the first cut. The repo currently focuses on authoring and review workflows for Terraform and Terragrunt only. Additional platform skills can be added later without changing the packaging model.
