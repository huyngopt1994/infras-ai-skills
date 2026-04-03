"""Core package for the obs-agent CLI."""

from importlib import metadata


try:  # pragma: no cover - dynamic metadata lookup
    __version__ = metadata.version("obs-agent")
except metadata.PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"


__all__ = ["__version__"]
