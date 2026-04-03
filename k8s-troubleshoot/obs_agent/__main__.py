"""Allows `python -m obs_agent` to run the CLI."""

from .cli import app


def main() -> None:
    app()


if __name__ == "__main__":  # pragma: no cover
    main()
