"""Coordinates collectors, processors, and presenters."""

from __future__ import annotations

from datetime import timedelta
from typing import Iterable, List, Sequence

from obs_agent.collectors import LokiCollector, PrometheusCollector
from obs_agent.collectors.base import BaseCollector
from obs_agent.llm import LLMPresenter
from obs_agent.models import CollectRequest, IncidentReport, Observation
from obs_agent.processors import ContextNormalizer, CorrelationEngine


class IncidentOrchestrator:
    def __init__(
        self,
        *,
        collectors: Sequence[BaseCollector] | None = None,
        normalizer: ContextNormalizer | None = None,
        correlator: CorrelationEngine | None = None,
        presenter: LLMPresenter | None = None,
    ) -> None:
        self.collectors = (
            list(collectors) if collectors else [PrometheusCollector(), LokiCollector()]
        )
        self.normalizer = normalizer or ContextNormalizer()
        self.correlator = correlator or CorrelationEngine()
        self.presenter = presenter or LLMPresenter()

    def analyze(
        self, *, service: str, namespace: str, window: timedelta, window_label: str
    ) -> IncidentReport:
        request = CollectRequest(service=service, namespace=namespace, window=window)
        observations = self._collect_all(request)
        context = self.normalizer.normalize(observations)
        hypotheses = self.correlator.rank(context)
        report = self.presenter.present(
            service=service,
            namespace=namespace,
            window_label=window_label,
            context=context,
            hypotheses=hypotheses,
        )
        return report

    def _collect_all(self, request: CollectRequest) -> List[Observation]:
        observations: List[Observation] = []
        for collector in self.collectors:
            observations.extend(list(collector.collect(request)))
        return observations


__all__ = ["IncidentOrchestrator"]
