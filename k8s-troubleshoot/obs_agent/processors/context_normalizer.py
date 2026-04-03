"""Utility that aligns heterogeneous observations into a common context."""

from __future__ import annotations

from typing import Iterable, List

from obs_agent.models import NormalizedContext, Observation, TimelineEvent


class ContextNormalizer:
    """Transforms raw observations into a timeline + anomaly summary."""

    def normalize(self, observations: Iterable[Observation]) -> NormalizedContext:
        obs_list: List[Observation] = list(observations)
        context = NormalizedContext(observations=obs_list)

        for obs in obs_list:
            if obs.kind == "metric":
                metric_name = obs.body.get("metric", "unknown")
                context.metrics_summary[metric_name] = float(obs.body.get("value", 0.0))

                if (
                    metric_name == "http_server_latency_p99"
                    and context.metrics_summary[metric_name] > 800
                ):
                    context.anomaly_flags.append("latency_spike")
                if (
                    metric_name == "http_server_error_ratio"
                    and context.metrics_summary[metric_name] > 0.05
                ):
                    context.anomaly_flags.append("error_rate_spike")
                if (
                    metric_name == "db_connection_saturation"
                    and context.metrics_summary[metric_name] > 0.8
                ):
                    context.anomaly_flags.append("db_saturation")

            else:
                description = obs.body.get("message", obs.kind.title())
                context.timeline.append(
                    TimelineEvent(
                        timestamp=obs.timestamps.observed, description=description
                    )
                )

        context.timeline.sort(key=lambda event: event.timestamp)
        return context


__all__ = ["ContextNormalizer"]
