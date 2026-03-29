---
name: github-actions
description: Create, review, validate, refactor, or troubleshoot GitHub Actions workflows, reusable workflows, and custom actions.
---

# GitHub Actions

Use this skill when the user is working on `.github/workflows/*.yml`, reusable workflows, `action.yml`, CI/CD automation, release pipelines, or GitHub Actions security and reliability issues.

## Outcomes

- Scaffold GitHub Actions workflows that are readable, secure, and maintainable
- Review existing workflows for broken triggers, unsafe permissions, and fragile execution patterns
- Fix workflow syntax, matrix, caching, concurrency, and dependency issues
- Explain GitHub Actions behavior, token scopes, and fork safety clearly

## Workflow

1. Inspect the repository layout first:
   - `.github/workflows/`
   - local actions such as `.github/actions/`
   - release or automation files that workflows call
2. Identify the workflow type:
   - CI validation
   - deploy/release
   - reusable workflow
   - scheduled automation
   - custom action
3. Verify trigger trust boundaries before editing:
   - internal branch pushes
   - same-repo pull requests
   - fork pull requests
   - manual dispatch
   - scheduled or tag-based release flows
4. Start with minimal top-level `permissions`, then elevate only per job when required.
5. Keep action versions deliberate:
   - prefer pinned SHAs for external actions when the repo values strict supply-chain control
   - otherwise pin to a stable major and call out the tradeoff
6. Add `concurrency`, caching, and matrix logic only when they materially improve the workflow.
7. Keep secrets out of untrusted execution paths, especially fork-triggered pull requests.
8. After editing, run the strongest local lint or validation available.

## Authoring Rules

- Prefer workflow-level `permissions: read-all` or explicit minimal scopes over broad write defaults.
- Do not use `pull_request_target` unless the repository actually needs privileged behavior and the trust model is explicit.
- Avoid passing repository secrets to jobs that can execute code from forks.
- Use `concurrency` for deploy, release, and long-running branch workflows to avoid stale runs.
- Prefer reusable workflows when multiple repositories or directories share the same pipeline contract.
- Keep `uses:` entries explicit and versioned.
- Keep job names human-readable and stable so required checks stay predictable.
- Use caching only when cache keys are deterministic and the speedup is real.
- Prefer OIDC or GitHub App auth over long-lived cloud credentials when the platform supports it.
- Reuse `examples/basic-ci.yml` when the user wants a clean CI baseline.

## Review Priorities

When reviewing or debugging GitHub Actions, check in this order:

1. Broken trigger logic or branch/path filters
2. Invalid permissions or over-privileged `GITHUB_TOKEN` usage
3. Fork safety issues:
   - secrets exposed to untrusted code
   - unsafe `pull_request_target` behavior
   - writes from untrusted contexts
4. Incorrect job dependencies, matrix expansion, or output wiring
5. Action version drift, deprecated actions, or missing pinning strategy
6. Reliability gaps:
   - no concurrency control for deploys
   - missing timeouts
   - missing retry-safe logic
   - cache misuse

## Validation Loop

Use what exists in the target repo first. Prefer this order when available:

```bash
actionlint .github/workflows/*.yml
yamllint .github/workflows/
gh workflow view <workflow-name>
```

If the repo uses local dry-run tooling such as `act`, include it when Docker and runner assumptions make the result meaningful.

If validation tooling or network access is unavailable, do a manual review and say exactly what could not be verified.

## Best-Practice Notes

- GitHub documents that `GITHUB_TOKEN` should have the least required access and that unspecified permissions become `none` when any permission is declared.
- GitHub also documents that `GITHUB_TOKEN` events usually do not recursively trigger new workflow runs, except for dispatch-style events.
- For protected delivery flows, prefer environment approvals, rulesets, and branch protections over ad hoc shell logic.

## Delivery Standard

Always leave the user with:

- the workflow pattern you chose and why it fits
- the files changed or recommended
- the validation commands run
- unresolved risks around permissions, secrets exposure, pinning, or release safety
