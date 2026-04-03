"""Command line entrypoint for obs-agent."""

from __future__ import annotations

from datetime import timedelta
import re
from typing import Iterable

import typer
from rich.console import Console
from rich.table import Table

from obs_agent import __version__
from obs_agent.orchestrator import IncidentOrchestrator
from obs_agent.models import IncidentReport

app = typer.Typer(help="AI-assisted Kubernetes incident triage", no_args_is_help=True)
console = Console()

_DURATION_PATTERN = re.compile(r"^(?P<value>\d+)(?P<unit>[smhd])$")


def _parse_window(value: str) -> timedelta:
    match = _DURATION_PATTERN.match(value.strip())
    if not match:
        raise typer.BadParameter("Use formats like 10m, 2h, 45s")

    units = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    seconds = int(match.group("value")) * units[match.group("unit")]
    return timedelta(seconds=seconds)


def _humanize(duration: timedelta) -> str:
    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    parts: list[str] = []
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    if seconds and not parts:
        parts.append(f"{seconds}s")
    return "".join(parts) or "0s"


def _render_report(report: IncidentReport, show_hypotheses: bool) -> None:
    console.rule("Incident Summary")
    console.print(
        f"Service: [bold]{report.service}[/]  Namespace: [bold]{report.namespace}[/]"
    )
    console.print(f"Window: {report.window_label}")
    console.print(f"Summary: {report.summary}")
    console.print(f"Likely cause ({report.confidence:.0%}): [bold]{report.cause}[/]")

    evidence_table = Table(title="Evidence", show_lines=True)
    evidence_table.add_column("#")
    evidence_table.add_column("Signal")
    for idx, item in enumerate(report.evidence, start=1):
        evidence_table.add_row(str(idx), item)
    console.print(evidence_table)

    timeline_table = Table(title="Timeline")
    timeline_table.add_column("Event")
    for row in report.timeline:
        timeline_table.add_row(row)
    console.print(timeline_table)

    next_table = Table(title="Next Actions")
    next_table.add_column("Command / Task")
    for step in report.next_actions:
        next_table.add_row(step)
    console.print(next_table)

    if show_hypotheses:
        hypo_table = Table(title="Hypotheses", show_lines=True)
        hypo_table.add_column("Label")
        hypo_table.add_column("Confidence")
        hypo_table.add_column("Evidence")
        for hypo in report.raw_hypotheses:
            hypo_table.add_row(
                hypo.label,
                f"{hypo.confidence:.0%}",
                "\n".join(hypo.supporting_evidence),
            )
        console.print(hypo_table)


@app.command()
def analyze(
    service: str = typer.Argument(..., help="Target service or workload"),
    namespace: str = typer.Option(
        ..., "--namespace", "-n", help="Target Kubernetes namespace"
    ),
    since: str = typer.Option(
        "10m", "--since", "-s", help="Lookback window (e.g. 10m, 2h)"
    ),
    explain: bool = typer.Option(False, "--explain", help="Show ranked hypotheses"),
) -> None:
    """Correlate metrics/logs/state to craft an incident report."""

    window = _parse_window(since)
    orchestrator = IncidentOrchestrator()
    report = orchestrator.analyze(
        service=service,
        namespace=namespace,
        window=window,
        window_label=_humanize(window),
    )
    _render_report(report, explain)


@app.command()
def version() -> None:
    """Print the obs-agent version."""

    console.print(f"obs-agent {__version__}")


if __name__ == "__main__":  # pragma: no cover
    app()
