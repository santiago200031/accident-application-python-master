from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any, ClassVar

import httpx


class Incident:
    """Base class for a single buggy scenario.

    Subclasses declare the ``incident_id`` and ``mode`` that identify them and
    implement ``run`` so that calling it raises the intended exception.
    """

    incident_id: ClassVar[str]
    mode: ClassVar[str]

    def run(self) -> Any:  # pragma: no cover - abstract-ish
        def run(self, numerator: int | None = None, denominator: int | None = None) -> float:
            if numerator is None or denominator is None:
                raise ValueError("numerator and denominator must be provided")
            if denominator == 0:
                raise ZeroDivisionError("Denominator cannot be zero")
            return numerator / denominator


class DivideByZeroIncident(Incident):
    incident_id = "inc-2026-001"
    mode = "divide-by-zero"

    def run(self) -> float:
        numerator = 5
        denominator = 0
        # Raises ZeroDivisionError.
        return numerator / denominator


class BadCastIncident(Incident):
    incident_id = "inc-2026-002"
    mode = "bad-cast"

    def run(self) -> float:
        value = "not-a-number"
        # Raises ValueError.
        return float(value)


class MissingFileIncident(Incident):
    incident_id = "inc-2026-003"
    mode = "missing-file"

    # Path is guaranteed not to exist in this repo.
    target: ClassVar[str] = "data/does-not-exist.txt"

    def run(self) -> str:
        # Raises FileNotFoundError.
        return Path(self.target).read_text(encoding="utf-8")


class IndexErrorIncident(Incident):
    incident_id = "inc-2026-004"
    mode = "index-error"

    def run(self) -> str:
        items = ["only-one"]
        # Raises IndexError.
        return items[10]


class NetworkChaosIncident(Incident):
    incident_id = "inc-2026-005"
    mode = "network-chaos"

    # Port 9 is the well-known "discard" port; nothing listens by default,
    # so the request is guaranteed to fail with a transport error.
    endpoint: ClassVar[str] = "http://127.0.0.1:9/nowhere"

    def run(self) -> dict:
        # Raises httpx.ConnectError (or a related transport error).
        response = httpx.get(self.endpoint, timeout=0.5)
        return response.json()


class NoneDereferenceIncident(Incident):
    incident_id = "inc-2026-006"
    mode = "none-dereference"

    def run(self) -> int:
        value: dict | None = self._maybe_get()
        # Raises TypeError: 'NoneType' object is not subscriptable.
        return value["count"]  # type: ignore[index]

    @staticmethod
    def _maybe_get() -> dict | None:
        # Always returns None in this scenario.
        return None


class BranchChaosIncident(Incident):
    incident_id = "inc-2026-007"
    mode = "branch-chaos"

    def run(self) -> str:
        # ``false`` always exits with status 1. With ``check=True`` this raises
        # subprocess.CalledProcessError.
        result = subprocess.run(
            ["false"], capture_output=True, text=True, check=True
        )
        return result.stdout


class RemediationWorkflowIncident(Incident):
    """A tiny multi-step workflow that fails partway through."""

    incident_id = "inc-2026-008"
    mode = "remediation-workflow"

    def run(self) -> Any:
        data = self._load_data()
        processed = self._process(data)
        # Raises KeyError: the expected key was never produced upstream.
        return processed["missing_key"]

    @staticmethod
    def _load_data() -> list[dict[str, int]]:
        return [{"value": 1}, {"value": 2}, {"value": 3}]

    @staticmethod
    def _process(rows: list[dict[str, int]]) -> dict[str, int]:
        return {"total": sum(row["value"] for row in rows)}


# Ordered list of incidents that make up the main cycle. Order matches the
# fixtures served by the external ``project-logs-provider`` WireMock.
INCIDENTS: list[type[Incident]] = [
    DivideByZeroIncident,
    BadCastIncident,
    MissingFileIncident,
    IndexErrorIncident,
    NetworkChaosIncident,
    NoneDereferenceIncident,
    BranchChaosIncident,
    RemediationWorkflowIncident,
]
