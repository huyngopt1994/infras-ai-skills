"""Stub Loki collector for log slices."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Iterable
from uuid import uuid4

from obs_agent.collectors.base import BaseCollector
from obs_agent.models import (
    CollectRequest,
    Observation,
    ObservationScope,
    ObservationTimestamps,
)


class LokiCollector(BaseCollector):
    name = "loki"

    def collect(self, request: CollectRequest) -> Iterable[Observation]:
        scope = ObservationScope(service=request.service, namespace=request.namespace)
        ts = ObservationTimestamps(observed=datetime.now(timezone.utc))

        log_line = Observation(
            id=str(uuid4()),
            kind="log",
            source=self.name,
            scope=scope,
            timestamps=ts,
            body={
                "level": "ERROR",
                "message": "db timeout error during checkout",
                "component": "checkout-api",
            },
        )

        rollout_line = Observation(
            id=str(uuid4()),
            kind="event",
            source=self.name,
            scope=scope,
            timestamps=ts,
            body={
                "message": "rollout started",
                "component": "deployment/checkout-api",
            },
        )

        return [log_line, rollout_line]


__all__ = ["LokiCollector"]
