---
name: infra-kit
description: Turn an infra ticket into a lightweight spec, implementation plan, task list, and implementation notes (with optional Confluence-ready output).
---

# Infra Kit

Use this skill to run a repeatable workflow from an incoming ticket (Jira/GitHub/Slack/Email) to:

- a clear problem statement and acceptance criteria
- an implementation plan with rollout/rollback and verification
- an executable task list
- implementation notes and a copy/paste Confluence summary

This framework focuses on infra delivery artifacts that are easy to review and operate.

For the end-to-end mapping across skills, see `docs/infras-kit/flow.md`.

## Output Rules

- Write the deliverables to Markdown files in the repo (not only chat output).
- Prefer `docs/infras-kit/work-items/<id>-<slug>/`.
- Keep docs skimmable. Push deep details into `implementation-notes.md`.

## Quick Start

1. Create a work-item directory and starter files:

```bash
bash infras-kit-plugin/skills/infra-kit/scripts/new-work-item.sh "<short title>" \
  --id "<TICKET-ID>" \
  --link "<ticket url>"
```

2. Fill in `ticket.md`, then generate `plan.md` and `tasks.md`.
3. Execute tasks, using domain skills for the actual work:

- use `infra-kit.iac` for Terraform/Terragrunt changes
- use `infra-kit.helm` for chart work
- use `infra-kit.k8s-doctor` for runtime debugging
- use `infra-kit.github` for repo and CI/CD changes
- use `infra-kit.audit` to review before merge/release

## Workflow

1. **Intake (ticket.md)**
   - restate the problem and intended outcome
   - list acceptance criteria and explicit non-goals
   - capture constraints (cloud, regions, compliance, timelines)
   - label unknowns as `[NEEDS CLARIFICATION: ...]`
2. **Spec (spec.md)**
   - translate ticket into an infra-focused spec: desired behavior, SLO/SLA impact, security boundaries
   - define “done” in testable terms
3. **Plan (plan.md)**
   - approach, risks, dependencies
   - rollout steps and explicit rollback
   - verification commands and expected signals
   - operational ownership: alerts/runbooks, cost notes
4. **Tasks (tasks.md)**
    - produce a checklist with small steps
    - tag each task with the intended skill (e.g., `[infra-kit.iac]`, `[infra-kit.helm]`)
   - mark parallelizable tasks with `[P]`
5. **Implement (implementation-notes.md)**
   - record what changed, gotchas, and final verification outputs
6. **Report (confluence.md)**
   - write a concise update suitable for Confluence/Jira comment

## Guardrails

- Don’t invent requirements. Ask when unknown.
- Don’t propose destructive rollouts without a rollback.
- Keep “plan” separate from “implementation”; avoid code dumps in `plan.md`.

## Template Locations

- `docs/infras-kit/work-items/<id>-<slug>/ticket.md`
- `docs/infras-kit/work-items/<id>-<slug>/spec.md`
- `docs/infras-kit/work-items/<id>-<slug>/plan.md`
- `docs/infras-kit/work-items/<id>-<slug>/tasks.md`
- `docs/infras-kit/work-items/<id>-<slug>/implementation-notes.md`
- `docs/infras-kit/work-items/<id>-<slug>/confluence.md`
