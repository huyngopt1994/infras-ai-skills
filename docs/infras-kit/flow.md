# Infras-Kit Problem-Solving Flow

This repo’s skills are designed to work together as a repeatable delivery workflow.

## Default Flow

1. Intake the request into a work item: create `docs/infras-kit/work-items/<nnn>-<slug>/` with `infra-kit`.
2. Frame the problem: clarify scope, impact, unknowns, and success criteria.
3. Research only what is uncertain or version-dependent.
4. Design the change when it’s non-trivial or high blast radius.
5. Write an implementation plan: rollout, rollback, verification, ownership.
6. Break down tasks: small steps, explicit skills, parallelizable where safe.
7. Implement using the domain skill that matches the artifact being changed.
8. Validate locally with the strongest deterministic checks available.
9. Audit for cross-cutting risks before merge/release.
10. Report back (Confluence/Jira comment) with plan, status, and evidence.

## Skill Mapping

- `infra-kit`: creates the work-item folder and provides the lightweight spec/plan/tasks templates.
- `infra-kit.thinking`: best when the ticket is ambiguous, incident-like, or you need hypotheses and evidence tables.
- `infra-kit.research`: best when the right answer depends on versions, vendor docs, quotas, or nuanced defaults.
- `infra-kit.design`: best for migrations, networking, platform changes, and anything requiring explicit rollout/rollback.
- `infra-kit.iac`: implement/review Infrastructure-as-Code with Terraform and/or Terragrunt.
- `infra-kit.helm`: implement/review Helm charts and workload defaults.
- `infra-kit.k8s-doctor`: read-only debugging to isolate the broken hop in Pod -> Service -> routing.
- `infra-kit.github`: implement/review repository governance and GitHub Actions workflows.
- `infra-kit.audit`: pre-merge/release audit for least privilege, release safety, OWASP exposure, and well-architected alignment.

## Standard Artifacts

Within `docs/infras-kit/work-items/<nnn>-<slug>/`:

- `ticket.md`: intake, constraints, acceptance criteria, unknowns
- `spec.md`: desired behavior and testable “done”
- `plan.md`: approach, risks, rollout/rollback, verification, ownership
- `tasks.md`: executable steps tagged by skill
- `implementation-notes.md`: what changed + validation evidence
- `confluence.md`: short update to paste into Confluence/Jira
