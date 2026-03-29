# Contributing

Keep this repo narrow and practical. New skills should improve delivery quality, not just add more text.

## Skill Standard

Every new skill should include:

- `SKILL.md` with a clear trigger description and an opinionated workflow
- at least one reusable example when the domain has a stable baseline shape
- a validation path when deterministic local checks are realistic
- README updates for install, discovery, and example prompts when the skill is shipped

## Design Rules

- Prefer one strong skill over multiple thin variants unless the split materially improves triggering.
- Bundle scripts when validation or generation logic is repeatable.
- Keep guidance concrete and reviewable; avoid long philosophy sections inside skills.
- Reuse examples and helper scripts instead of re-explaining the same patterns in multiple places.
- Make skipped validation explicit when tooling, credentials, or network access are missing.

## Repo Scope

Prioritize infrastructure, Kubernetes, IaC, CI/CD, and repository hygiene workflows that teams repeatedly need in practice.
