---
name: terragrunt
description: Create, review, validate, refactor, or troubleshoot Terragrunt HCL layouts, root.hcl patterns, dependencies, stacks, and environment wiring.
---

# Terragrunt

Use this skill when the user is working on Terragrunt layouts, `root.hcl`, `terragrunt.hcl`, stacks, dependency wiring, remote state configuration, or multi-environment infrastructure orchestration.

## Outcomes

- Scaffold clean Terragrunt folder structures for single or multiple environments
- Fix broken includes, locals, dependencies, and input propagation
- Model upstream/downstream module contracts with `dependency` blocks and safe mock outputs
- Review Terragrunt layouts for maintainability and execution safety
- Explain how Terragrunt coordinates Terraform or OpenTofu modules

## Workflow

1. Inspect the directory layout first.
2. Identify the pattern in use:
   - single environment
   - multi-environment
   - root plus per-environment overlays
   - stacks/catalog model
3. Confirm where shared configuration actually lives:
   - `root.hcl`
   - `env.hcl`
   - `account.hcl`
   - `region.hcl`
4. Before editing, verify that every `find_in_parent_folders`, `read_terragrunt_config`, and `dependency` path makes sense from the file that calls it.
5. Keep the root config generic unless the repo clearly uses an environment-aware root.
6. Push environment-specific values to the nearest sensible layer instead of leaking them into every child module.
7. After editing, run HCL formatting and Terragrunt validation commands when available.
8. Ensure Terraform inputs include a consistent labeling contract for downstream resources.
9. If labels or tags are not defined by the user, ask for them or default to:
   - `project`
   - `environment`
   - `owner`
   - `managed_by`
   - `cost_center` when relevant

## Authoring Rules

- Prefer `root.hcl` for modern root configuration unless the repo is intentionally on legacy naming.
- Keep remote state generation consistent across environments.
- Use `include` and shared locals to remove duplication, not to hide important inputs.
- Use `dependency` blocks only where data flow is real and ordering matters.
- Prefer `dependency` over copy-pasting IDs or CIDRs across units when one module already owns that output.
- Add `mock_outputs` only for commands that need them, such as `validate`, and keep the mocked shape aligned with the real Terraform outputs.
- Keep `inputs` explicit at the edge of each unit so module contracts stay readable.
- Avoid brittle path logic when a simpler structure would work.
- When stacks are used, keep units and shared conventions predictable.
- Prefer passing shared labels through `inputs` so Terraform modules can tag resources consistently.
- Reuse `examples/live-aws/` when the user wants a standard multi-environment baseline, including a simple `app -> vpc` dependency pattern.

## Review Priorities

When reviewing or debugging Terragrunt, check in this order:

1. Broken include chains and bad parent-folder lookups
2. Wrong dependency paths or missing mock outputs
3. Input shape mismatches between Terragrunt and Terraform modules
4. Remote state collisions or inconsistent state key patterns
5. Environment leakage:
   - prod values in shared root files
   - hardcoded regions/accounts in child units
   - duplicated locals that should be centralized
6. Execution safety:
   - unexpected run-all blast radius
   - hidden dependencies
   - fragile ordering assumptions

## Validation Loop

Prefer the repo’s own scripts first. Otherwise use the strongest available subset:

```bash
terragrunt hcl fmt
terragrunt hcl validate
terragrunt init
terragrunt validate
terragrunt plan
```

For larger layouts, check dependency execution paths carefully before any `run --all` or legacy `run-all` command.

If provider/module docs are needed for third-party sources, look them up before changing configuration.

Bundled helper:

```bash
bash scripts/validate_terragrunt.sh <path>
```

## Delivery Standard

Always leave the user with:

- the chosen layout pattern and why it fits
- the concrete files changed or recommended
- the validation commands run
- any unresolved risks around dependency order, shared state, or environment separation
