"""Basic smoke tests for the CLI."""

from typer.testing import CliRunner

from obs_agent.cli import app


runner = CliRunner()


def test_analyze_command_runs() -> None:
    result = runner.invoke(
        app, ["analyze", "checkout-api", "--namespace", "payments", "--since", "5m"]
    )
    assert result.exit_code == 0
    assert "checkout-api" in result.stdout
    assert "Likely cause" in result.stdout
