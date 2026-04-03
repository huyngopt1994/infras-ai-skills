"""Shared collector interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

from obs_agent.models import CollectRequest, Observation


class BaseCollector(ABC):
    name: str

    @abstractmethod
    def collect(self, request: CollectRequest) -> Iterable[Observation]:
        """Return observations for the provided request window."""


__all__ = ["BaseCollector"]
