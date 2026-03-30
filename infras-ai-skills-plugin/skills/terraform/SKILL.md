---
name: terraform
description: Create, review, validate, refactor, or troubleshoot Terraform .tf and .tfvars files, modules, providers, backends, plans, and security issues.
---

# Terraform

Use this skill when the user is working on Terraform modules, stacks, providers, backends, variables, outputs, plans, or IaC review.

## Outcomes

- Scaffold new Terraform code that is readable and reusable
- Review existing Terraform for correctness, drift risk, and security gaps
- Fix validation failures and broken module wiring
- Explain plans, state interactions, and provider behavior clearly

## Workflow

1. Inspect the current Terraform layout before changing files.
2. Identify provider versions, module sources, backend strategy, and environment assumptions.
3. If the request uses non-HashiCorp or unfamiliar providers/modules, look up the exact documentation before writing code.
4. Prefer standard file separation:
   - `main.tf`
   - `variables.tf`
   - `outputs.tf`
   - `versions.tf`
   - `providers.tf`
   - `backend.tf` when backend config belongs in code
5. Keep modules reusable:
   - typed variables
   - useful descriptions
   - constrained defaults only when safe
   - stable outputs
   - tags/labels via locals instead of copy-paste
6. Favor data sources for dynamic discovery instead of hardcoded IDs when practical.
7. Protect critical resources with lifecycle settings only when the behavior is intentional and explained.
8. After editing, run the strongest local validation available.
9. Always include labels or tags for managed resources when the provider supports them.
10. If the user did not specify a label/tag contract, ask for one or apply a sensible default set such as:
    - `project`
    - `environment`
    - `owner`
    - `managed_by`
    - `cost_center` when relevant

## Authoring Rules

- Prefer explicit `required_version` and `required_providers`.
- Pin provider and module versions to a deliberate compatible range.
- Use `locals` for repeated naming, tagging, and derived values.
- Standardize labels/tags across all resources in the module whenever the provider supports metadata fields.
- Keep variable names and resource names descriptive and in `snake_case`.
- Model IAM roles, bindings, and policies with least-privilege scopes for AWS and GCP unless the user explicitly accepts broader rights.
- Add validation blocks for variables that have tight accepted values.
- Avoid embedding secrets in code or example tfvars.
- Avoid overusing `depends_on`; rely on data flow first.
- Do not create giant single-file modules unless the repo already follows that style.
- Reuse `examples/minimal-module/` as the default starter shape when the user wants a clean baseline.

## Review Priorities

When reviewing or debugging Terraform, check in this order:

1. Syntax and formatting issues
2. Broken references, types, and module inputs
3. Provider or backend misconfiguration
4. Destructive lifecycle or state-move risks
5. Security gaps:
    - open ingress
    - missing encryption
    - unsafe IAM permissions or over-broad role bindings
   - plaintext secrets
   - public exposure by default
6. Maintainability issues:
   - duplicated logic
   - weak variable contracts
   - missing outputs
   - unclear naming

## Validation Loop

Use what exists in the target repo. Prefer this order when available:

```bash
terraform fmt -recursive
terraform init
terraform validate
terraform plan
```

If the repo uses additional tooling, include it:

```bash
tflint
checkov -d .
trivy config .
```

If a command cannot run because credentials, network, or tooling are unavailable, say exactly what was skipped and continue with the strongest offline review possible.

Bundled helper:

```bash
bash scripts/validate_terraform.sh <path>
```

## Delivery Standard

Always leave the user with:

- the changed files or recommended file layout
- the key assumptions you made
- any commands run for validation
- unresolved risks, especially around state, credentials, and destructive changes
