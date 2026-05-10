## Goal

Identify process-oriented skills that would materially improve this repo's current infra skill set (k8s, IaC, Helm, GitHub, audit/design/research/thinking).

## Current Skill Set (This Repo)

From the available skills list in this workspace:

- `infra-kit.domain.github`: GitHub repo + CI/CD assets
- `infra-kit.domain.helm`: Helm charts/templates/values
- `infra-kit.domain.iac`: Terraform/Terragrunt
- `infra-kit.domain.k8s-doctor`: Kubernetes debugging (read-only kubectl flows)
- `infra-kit.workflow`: ticket -> lightweight spec/plan/notes
- `infra-kit.workflow.audit`: security/reliability/compliance delivery hygiene
- `infra-kit.workflow.design`: requirements/SLOs/security/rollout/ops ownership
- `infra-kit.workflow.research`: research with citations
- `infra-kit.workflow.thinking`: decision hygiene for incidents/migrations/trade-offs

Summary: strong domain depth (k8s/IaC/Helm/GitHub) and strong "thinking/spec/design/audit" workflows.

## Candidate Process Skills To Add

The current library is strong on infra domains and higher-level reasoning. The main opportunity is to add cross-cutting process skills that apply regardless of domain (k8s/IaC/Helm/GitHub).

## Overlap vs Gaps

Overlap (same intent, different framing):

- Requirements clarification and trade-offs: already covered by `infra-kit.workflow.design` + `infra-kit.workflow.thinking`.
- Kubernetes-specific troubleshooting: covered by `infra-kit.domain.k8s-doctor`.

Clear gaps where process skills are additive:

1. **Verification discipline**
   - We have hallucination guardrails in `infra-kit.workflow.thinking`, but not an explicit "definition of fixed" verification checklist that applies to infra, CI, Helm, IaC, etc.

2. **Execution mechanics for multi-step work**
   - `infra-kit.workflow` covers spec/plan creation, but we can tighten task granularity conventions and "checkpointed execution".

3. **Code review loop hygiene**
   - Our current skills focus more on producing artifacts than on the iterative review loop (PR readiness and responding to review feedback).

4. **Safe parallelization + isolation**
   - Useful when we have independent domains (e.g., Helm + GitHub Actions + Terraform updates) that can be worked in parallel.

5. **"Prove It" stance for infra repos**
   - The underlying discipline maps to infra via "tests" such as `terraform validate/plan`, policy checks, `helm template`, `kubeconform`, `conftest`, CI workflows, smoke checks.
   - We currently do not have a single, explicit posture that says "prove it fails, then prove it passes" for infra automation.

Lower-value (for an infra-first skill library) but still helpful:

- A branch hygiene/cleanup skill (PR vs merge vs keep branch, and cleanup steps).
- A skill-authoring standard (if you expect to iteratively expand the skill library).

## Recommendations (Highest ROI)

If you want the smallest set of additions that would noticeably increase effectiveness for infra work:

1. **Add `infra-kit.workflow.verify`** (Recommended)
   - Infra-specific verification checklist that sits "after" any domain skill.
   - Outcome: fewer regressions, fewer ambiguous "done" states, cleaner handoffs.

2. **Add `infra-kit.workflow.debug`**
   - A tighter, evidence-driven debugging loop for day-to-day break/fix. Use `infra-kit.workflow.thinking` when stakes/ambiguity are high, and pair with domain skills (e.g., `k8s-doctor`) when applicable.
   - Outcome: faster root-cause isolation, fewer speculative fixes.

3. **Tighten plan->execute mechanics in `infra-kit.workflow`**
   - Adopt a strict task format (small, verifiable, file paths + exact commands) and explicit checkpoints/stop conditions.
   - Outcome: less drift between plan and implementation, easier parallel work.

4. **Add `infra-kit.workflow.review`**
   - PR readiness checklist + responding to review feedback (Terraform/Helm/Actions oriented).
   - Outcome: higher-quality PRs, faster iteration with reviewers.

## Suggested Integration Approach (Minimal Change)

- Keep domain skills (`k8s-doctor`, `iac`, `helm`, `github`) as-is.
- Use `workflow.thinking` when the situation is ambiguous or high-stakes.
- Add (or extend) one cross-cutting skill for:
  - "verification before completion" (definition of fixed)
  - "systematic debugging" (root cause loop)
- Extend `infra-kit.workflow` artifacts to include:
  - a tighter task list format (small, verifiable, file paths + commands)
  - explicit checkpoints and stop conditions

## Concrete New Skills To Create (If You Choose To Expand)

- `infra-kit.workflow.verify`: post-change verification checklist across domains (k8s/IaC/Helm/GitHub)
- `infra-kit.workflow.debug`: generic debugging loop (not k8s-specific), pairs with `infra-kit.domain.k8s-doctor` when K8s is in scope
- `infra-kit.workflow.review`: PR readiness + responding to review feedback (IaC/Helm/Actions oriented)

## Open Questions (So We Don’t Overbuild)

- Do you want this repo to be **infra-only**, or also cover general SDLC work (TDD, branch workflow) for application code?
- Do you have a preferred branching model (trunk-based vs GitFlow) that would affect whether `using-git-worktrees` / `finishing-a-development-branch` should be formalized?
- What verification tooling is standard in your org (e.g., `terraform test`, `tflint`, `checkov`, `helm unittest`, `kubeconform`, `conftest`, `gator`, `policy-as-code`), so the verification skill can be concrete?
