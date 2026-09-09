from __future__ import annotations

import subprocess

from incident_package.services.command_executor_service import BranchChaosIncident


def _make_incident() -> BranchChaosIncident:
    try:
        return BranchChaosIncident()
    except TypeError:
        return object.__new__(BranchChaosIncident)


def _patch_subprocess_run(monkeypatch, *, returncode: int, stdout: str) -> None:
    def fake_run(args, *popenargs, **kwargs):
        check = kwargs.get("check", False)
        if check and returncode != 0:
            raise subprocess.CalledProcessError(returncode, args)
        return subprocess.CompletedProcess(
            args=args,
            returncode=returncode,
            stdout=stdout,
            stderr="",
        )

    monkeypatch.setattr(subprocess, "run", fake_run)


def test_run_returns_empty_stdout_for_failing_false_command(monkeypatch):
    incident = _make_incident()
    _patch_subprocess_run(monkeypatch, returncode=1, stdout="")
    assert incident.run() == ""


def test_execute_shell_command_returns_stdout_for_failing_command(monkeypatch):
    incident = _make_incident()
    _patch_subprocess_run(monkeypatch, returncode=1, stdout="partial\n")
    assert incident.execute_shell_command(["false"]) == "partial\n"


def test_execute_shell_command_returns_stdout_for_successful_command(monkeypatch):
    incident = _make_incident()
    _patch_subprocess_run(monkeypatch, returncode=0, stdout="ok\n")
    assert incident.execute_shell_command(["true"]) == "ok\n"