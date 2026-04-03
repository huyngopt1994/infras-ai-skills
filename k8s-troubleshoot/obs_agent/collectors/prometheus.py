"""Stub Prometheus collector to simulate metric readings."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Iterable, List
from uuid import uuid4

from obs_agent.collectors.base import BaseCollector
from obs_agent.models import (
    CollectRequest,
    Observation,
    ObservationScope,
    ObservationTimestamps,
)


class PrometheusCollector(BaseCollector):
    name = "prometheus"

    def collect(self, request: CollectRequest) -> Iterable[Observation]:
        now = datetime.now(timezone.utc)
        scope = ObservationScope(service=request.service, namespace=request.namespace)

        latency = Observation(
            id=str(uuid4()),
            kind="metric",
            source=self.name,
            scope=scope,
            timestamps=ObservationTimestamps(observed=now),
            body={
                "metric": "http_server_latency_p99",
                "value": 1200.0,
                "unit": "ms",
                "window_seconds": request.window.total_seconds(),
            },
        )

        error_rate = Observation(
            id=str(uuid4()),
            kind="metric",
            source=self.name,
            scope=scope,
            timestamps=ObservationTimestamps(observed=now),
            body={
                "metric": "http_server_error_ratio",
                "value": 0.081,
                "unit": "ratio",
                "window_seconds": request.window.total_seconds(),
            },
        )

        saturation = Observation(
            id=str(uuid4()),
            kind="metric",
            source=self.name,
            scope=scope,
            timestamps=ObservationTimestamps(observed=now),
            body={
                "metric": "db_connection_saturation",
                "value": 0.92,
                "unit": "ratio",
                "window_seconds": request.window.total_seconds(),
            },
        )

        return [latency, error_rate, saturation]


__all__ = ["PrometheusCollector"]
