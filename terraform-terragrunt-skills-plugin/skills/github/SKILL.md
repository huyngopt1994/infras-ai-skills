---
name: github
description: Create, review, standardize, or troubleshoot repository-level GitHub files such as CODEOWNERS, templates, rulesets guidance, and contributor workflows.
---

# GitHub Repository

Use this skill when the user is working on repository governance and collaboration files such as `.github/CODEOWNERS`, pull request templates, issue templates, `CONTRIBUTING.md`, release automation, labels strategy, or branch protection and ruleset guidance.

## Outcomes

- Scaffold repository governance files that keep contribution flow consistent
- Review GitHub repo configuration for unclear ownership, missing templates, and weak merge controls
- Standardize pull request and issue hygiene with lightweight defaults
- Explain how GitHub collaboration features fit together across templates, reviews, and protected branches

## Workflow

1. Inspect repository collaboration files first:
   - `.github/`
   - `CODEOWNERS`
   - `CONTRIBUTING.md`
   - pull request and issue templates
   - release or merge automation config
2. Identify the operating model:
   - single maintainer
   - team-owned repository
   - platform/shared service repo
   - open-source contributor flow
3. Keep ownership and review routing explicit before adding automation.
4. Prefer the smallest set of governance files that solve the real workflow problem.
5. When branch protection or rulesets are part of the ask, describe the GitHub settings alongside any repo files that support them.
6. After editing, verify that file locations match GitHub's expected discovery paths.

## Authoring Rules

- Use `CODEOWNERS` when review ownership matters, and keep patterns simple enough that maintainers can reason about them.
- Prefer pull request templates that collect decision-making context, testing notes, and rollout risk, not boilerplate filler.
- Use issue templates or forms only when triage quality is suffering; avoid over-structuring low-volume repos.
- Keep `CONTRIBUTING.md` actionable:
  - setup
  - validation commands
  - branch or PR expectations
  - release process when relevant
- Prefer protected branches and rulesets for merge controls instead of relying on convention alone.
- Keep automation-friendly labels and release notes conventions explicit if the repo uses them.
- Reuse `examples/` when the user wants a clean baseline for ownership or pull request hygiene.

## Review Priorities

When reviewing GitHub repository collaboration setup, check in this order:

1. Missing or wrong review ownership in `CODEOWNERS`
2. Merge safety gaps:
   - no required reviews
   - no required status checks
   - no protection on release branches
3. Missing pull request guidance for testing, risk, and rollback notes
4. Missing contribution instructions for local validation and branching flow
5. Overly complicated templates or ownership patterns that people will ignore

## Best-Practice Notes

- GitHub documents that pull request templates and issue templates standardize the information contributors provide.
- GitHub documents that `CODEOWNERS`, protected branches, and rulesets help ensure the right reviewers and checks are applied before merge.
- Keep file placement aligned with GitHub discovery rules, such as `.github/PULL_REQUEST_TEMPLATE.md` or `.github/ISSUE_TEMPLATE/`.

## Delivery Standard

Always leave the user with:

- the collaboration pattern you chose and why it fits
- the files changed or recommended
- any GitHub UI settings that still need to be enabled manually
- unresolved risks around ownership gaps, weak branch protection, or template sprawl
