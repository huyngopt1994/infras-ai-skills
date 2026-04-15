# Infras AI Skills

Opinionated, practical skills for infrastructure engineering work: Kubernetes troubleshooting, IaC authoring and review, CI/CD hardening, repository hygiene, and structured thinking for design and research.

These skills are intended to raise engineering quality (security, reliability, operability, maintainability) rather than only generate configuration quickly.

## What This Folder Is

Each subfolder is a single skill.

- `SKILL.md`: the trigger description plus workflow and guardrails
- `examples/`: optional reusable templates and baselines
- `scripts/`: optional deterministic helpers for validation/collection

## Skill Catalog

- `terraform`: scaffold/review/validate Terraform modules and stacks with least-privilege and safe defaults
- `terragrunt`: design and troubleshoot Terragrunt layouts, dependencies, and environment wiring
- `helm`: scaffold/review/harden Helm charts, templates, and workload defaults
- `k8s-doctor`: read-only-first Kubernetes debugging across Pods, Services, endpoints, and routing layers
- `github-actions`: harden GitHub Actions workflows for minimal permissions, fork safety, and maintainability
- `github`: repository governance and collaboration hygiene (CODEOWNERS, templates, contributor flow)
- `infra-auditor`: infrastructure and DevOps audits grounded in well-architected and OWASP-style controls
- `infra-thinking`: structured problem solving and decision hygiene for infra work
- `infra-design`: requirements-first infrastructure design with rollout/rollback and operational ownership
- `infra-research`: version-aware, source-backed research briefs with a concrete validation plan

## Usage Conventions

When invoking a skill, include:

- scope: paths, repo, environment
- intent: generate vs. review vs. troubleshoot
- constraints: cloud/provider, Kubernetes distro/version, compliance, timelines
- verification: which commands you want run (if any)

Examples:

```text
Use infra-thinking to triage an incident where API latency spiked after a deploy.
Use infra-design to propose a rollout plan for migrating from Ingress to Gateway API.
Use infra-research to compare AWS NLB + Ingress vs. Gateway API for our k8s version 1.29.
Use k8s-doctor to trace a 503 from ingress to Pod in namespace payments.
Use github-actions to review .github/workflows/release.yml for fork safety and token permissions.
```

## Deliverable Rules (Design + Research)

For design and research work, the default output is not a long chat response.

- Write deliverables to Markdown file(s) in the repo.
- If the content is large, split it into multiple Markdown files (keep each file narrow and skimmable).
- Prefer stable locations:
  - `docs/infra-design/<topic>/...`
  - `docs/infra-research/<topic>/...`

## Design Principles

- Evidence over vibes: cite files/lines/commands for reviews and debugging.
- Safe-by-default: reversible actions first, high-blast-radius actions require explicit approval.
- Least privilege: IAM, tokens, and RBAC should be explicit and minimal.
- DRY and maintainable: prefer reusable primitives over copy-paste configuration.
