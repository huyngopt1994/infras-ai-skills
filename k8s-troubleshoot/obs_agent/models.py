"""Shared data models used throughout the obs-agent pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional


@dataclass(slots=True)
class ObservationScope:
    service: str
    namespace: str


@dataclass(slots=True)
class ObservationTimestamps:
    observed: datetime


@dataclass(slots=True)
class Observation:
    id: str
    kind: str
    source: str
    scope: ObservationScope
    timestamps: ObservationTimestamps
    body: Dict[str, Any]


@dataclass(slots=True)
class CollectRequest:
    service: str
    namespace: str
    window: timedelta


@dataclass(slots=True)
class TimelineEvent:
    timestamp: datetime
    description: str


@dataclass(slots=True)
class NormalizedContext:
    observations: List[Observation] = field(default_factory=list)
    metrics_summary: Dict[str, float] = field(default_factory=dict)
    anomaly_flags: List[str] = field(default_factory=list)
    timeline: List[TimelineEvent] = field(default_factory=list)


@dataclass(slots=True)
class CorrelationHypothesis:
    label: str
    confidence: float
    supporting_evidence: List[str] = field(default_factory=list)


@dataclass(slots=True)
class IncidentReport:
    service: str
    namespace: str
    window_label: str
    summary: str
    cause: str
    confidence: float
    evidence: List[str]
    timeline: List[str]
    next_actions: List[str]
    raw_hypotheses: List[CorrelationHypothesis]
