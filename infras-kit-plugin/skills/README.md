# Infras Kit

Lightweight infrastructure delivery framework (ticket -> spec -> plan -> tasks) plus opinionated domain skills for IaC, Kubernetes, CI/CD, and repo governance.

The goal is to raise engineering quality (security, reliability, operability, maintainability) rather than only generate configuration quickly.

## What This Folder Is

Each subfolder is a single skill.

- `SKILL.md`: the trigger description plus workflow and guardrails
- `examples/`: optional reusable templates and baselines
- `scripts/`: optional deterministic helpers for validation/collection

## Skill Catalog

- `infra-kit.iac`: Terraform + Terragrunt authoring/review/validation
- `infra-kit.helm`: scaffold/review/harden Helm charts, templates, and workload defaults
- `infra-kit.k8s-doctor`: read-only-first Kubernetes debugging across Pods, Services, endpoints, and routing layers
- `infra-kit.github`: GitHub repo + Actions governance (CODEOWNERS, templates, branch protection guidance, workflow hardening)
- `infra-kit.audit`: infrastructure and DevOps audits grounded in well-architected and OWASP-style controls
- `infra-kit.thinking`: structured problem solving and decision hygiene for infra work
- `infra-kit.design`: requirements-first infrastructure design with rollout/rollback and operational ownership
- `infra-kit.research`: version-aware, source-backed research briefs with a concrete validation plan
- `infra-kit`: lightweight ticket -> spec -> plan -> tasks -> implementation notes workflow (includes Confluence-ready update template)

## Recommended Flow

If you want a consistent way to solve infra tickets end-to-end, use:

1. `infra-kit` to create `docs/infras-kit/work-items/...` and drive `ticket.md` -> `spec.md` -> `plan.md` -> `tasks.md`.
2. `infra-kit.thinking` when the request is ambiguous or incident-like.
3. `infra-kit.research` when behavior is version-dependent or requires vendor docs.
4. `infra-kit.design` for non-trivial changes that need explicit rollout/rollback.
5. Domain skills (`infra-kit.iac`, `infra-kit.helm`, `infra-kit.github`, `infra-kit.k8s-doctor`) to execute.
6. `infra-kit.audit` before merge/release to catch cross-cutting risks.

For the full mapping across skills and artifacts, see `docs/infras-kit/flow.md`.

## Usage Conventions

When invoking a skill, include:

- scope: paths, repo, environment
- intent: generate vs. review vs. troubleshoot
- constraints: cloud/provider, Kubernetes distro/version, compliance, timelines
- verification: which commands you want run (if any)

Examples:

```text
Use infra-kit.thinking to triage an incident where API latency spiked after a deploy.
Use infra-kit.design to propose a rollout plan for migrating from Ingress to Gateway API.
Use infra-kit.research to compare AWS NLB + Ingress vs. Gateway API for our k8s version 1.29.
Use infra-kit.k8s-doctor to trace a 503 from ingress to Pod in namespace payments.
Use infra-kit.github to review .github/workflows/release.yml for fork safety and token permissions.
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
