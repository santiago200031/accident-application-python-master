import subprocess
from types import SimpleNamespace

from incident_package.services import command_executor_service as command_executor_module
from incident_package.services.command_executor_service import BranchChaosIncident


def _make_branch_chaos_incident() -> BranchChaosIncident:
    return BranchChaosIncident.__new__(BranchChaosIncident)


def test_execute_shell_command_returns_empty_string_for_empty_args():
    incident = _make_branch_chaos_incident()
    assert incident.execute_shell_command([]) == ""


def test_execute_shell_command_returns_empty_string_when_false_command_fails(monkeypatch):
    def fake_run(*args, **kwargs):
        raise subprocess.CalledProcessError(1, ["false"])

    monkeypatch.setattr(command_executor_module.subprocess, "run", fake_run)
    incident = _make_branch_chaos_incident()
    assert incident.execute_shell_command(["false"]) == ""


def test_run_returns_empty_string_when_false_command_fails(monkeypatch):
    def fake_run(*args, **kwargs):
        raise subprocess.CalledProcessError(1, ["false"])

    monkeypatch.setattr(command_executor_module.subprocess, "run", fake_run)
    incident = _make_branch_chaos_incident()
    assert incident.run() == ""


def test_execute_shell_command_returns_stdout_on_success(monkeypatch):
    def fake_run(*args, **kwargs):
        return SimpleNamespace(stdout="ok")

    monkeypatch.setattr(command_executor_module.subprocess, "run", fake_run)
    incident = _make_branch_chaos_incident()
    assert incident.execute_shell_command(["true"]) == "ok"