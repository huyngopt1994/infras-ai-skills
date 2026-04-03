"""Simple correlation heuristics for the prototype."""

from __future__ import annotations

from typing import List

from obs_agent.models import CorrelationHypothesis, NormalizedContext


class CorrelationEngine:
    def rank(self, context: NormalizedContext) -> List[CorrelationHypothesis]:
        hypotheses: List[CorrelationHypothesis] = []

        metrics = context.metrics_summary
        flags = set(context.anomaly_flags)

        if {"latency_spike", "error_rate_spike"} <= flags and metrics.get(
            "db_connection_saturation", 0
        ) > 0.85:
            hypotheses.append(
                CorrelationHypothesis(
                    label="Database connection saturation",
                    confidence=0.82,
                    supporting_evidence=[
                        "p99 latency increased",
                        "error ratio jumped",
                        "DB saturation exceeded 85%",
                    ],
                )
            )

        if not hypotheses and "latency_spike" in flags:
            hypotheses.append(
                CorrelationHypothesis(
                    label="Recent rollout likely introduced latency",
                    confidence=0.55,
                    supporting_evidence=[
                        "Latency spike detected",
                        "Rollout event present",
                    ],
                )
            )

        if not hypotheses:
            hypotheses.append(
                CorrelationHypothesis(
                    label="No strong signal detected",
                    confidence=0.3,
                    supporting_evidence=["Insufficient correlated anomalies"],
                )
            )

        return hypotheses


__all__ = ["CorrelationEngine"]
