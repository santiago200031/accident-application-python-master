import subprocess

from incident_package.services.command_executor_service import BranchChaosIncident


def _make_incident() -> BranchChaosIncident:
    return object.__new__(BranchChaosIncident)


def test_run_returns_empty_string_for_failing_false_command(monkeypatch):
    calls = []

    def fake_run(command_args, **kwargs):
        calls.append(command_args)
        raise subprocess.CalledProcessError(1, command_args)

    monkeypatch.setattr(subprocess, "run", fake_run)
    incident = _make_incident()

    assert incident.run() == ""
    assert calls == [["false"]]


def test_execute_shell_command_returns_empty_string_for_failing_false_command(monkeypatch):
    def fake_run(command_args, **kwargs):
        raise subprocess.CalledProcessError(1, command_args)

    monkeypatch.setattr(subprocess, "run", fake_run)
    incident = _make_incident()

    assert incident.execute_shell_command(["false"]) == ""


def test_execute_shell_command_returns_stdout_for_successful_command(monkeypatch):
    def fake_run(command_args, **kwargs):
        return subprocess.CompletedProcess(
            args=command_args,
            returncode=0,
            stdout="ok\n",
            stderr="",
        )

    monkeypatch.setattr(subprocess, "run", fake_run)
    incident = _make_incident()

    assert incident.execute_shell_command(["some-command"]).strip() == "ok"