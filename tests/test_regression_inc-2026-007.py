import subprocess

from incident_package.services.command_executor_service import BranchChaosIncident


def test_execute_shell_command_returns_stdout_when_command_exits_nonzero(monkeypatch):
    expected_result = subprocess.CompletedProcess(
        args=["false"],
        returncode=1,
        stdout="expected diagnostic output\n",
        stderr="expected error output\n",
    )
    calls = []

    def fake_run(*args, **kwargs):
        calls.append((args, kwargs))
        return expected_result

    monkeypatch.setattr(subprocess, "run", fake_run)

    incident = BranchChaosIncident()
    output = incident.execute_shell_command(["false"])

    assert output == "expected diagnostic output\n"
    assert calls == [
        (
            (["false"],),
            {"capture_output": True, "text": True, "check": False},
        )
    ]


def test_run_does_not_raise_for_intentional_false_command(monkeypatch):
    def fake_run(command_args, **kwargs):
        assert command_args == ["false"]
        assert kwargs == {"capture_output": True, "text": True, "check": False}
        return subprocess.CompletedProcess(
            args=command_args,
            returncode=1,
            stdout="",
            stderr="",
        )

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert BranchChaosIncident().run() == ""