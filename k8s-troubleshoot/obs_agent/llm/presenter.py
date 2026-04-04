"""Mock presenter that emulates an LLM generated report."""

from __future__ import annotations

from typing import Iterable, List

from obs_agent.models import CorrelationHypothesis, IncidentReport, NormalizedContext


class LLMPresenter:
    def present(
        self,
        *,
        service: str,
        namespace: str,
        window_label: str,
        context: NormalizedContext,
        hypotheses: Iterable[CorrelationHypothesis],
    ) -> IncidentReport:
        hypotheses_list: List[CorrelationHypothesis] = list(hypotheses)
        best = hypotheses_list[0]

        summary = (
            f"{service} exhibits elevated latency and errors within {window_label}"
        )
        timeline_strings = [
            f"{event.timestamp:%H:%M:%S} {event.description}"
            for event in context.timeline
        ]

        next_actions = [
            "kubectl describe deploy {svc} -n {ns}".format(svc=service, ns=namespace),
            "Check database connection pool saturation",
            "Validate recent config or rollout",
        ]

        report = IncidentReport(
            service=service,
            namespace=namespace,
            window_label=window_label,
            summary=summary,
            cause=best.label,
            confidence=best.confidence,
            evidence=best.supporting_evidence,
            timeline=timeline_strings or ["No timeline events captured"],
            next_actions=next_actions,
            raw_hypotheses=hypotheses_list,
        )

        return report


__all__ = ["LLMPresenter"]
