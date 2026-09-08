import subprocess

import pytest

from incident_package.services.command_executor_service import BranchChaosIncident


def test_branch_chaos_tolerates_expected_nonzero_command_exit(monkeypatch):
    calls = []

    def fake_run(command_args, *, capture_output, text, check):
        calls.append(
            {
                "command_args": command_args,
                "capture_output": capture_output,
                "text": text,
                "check": check,
            }
        )
        assert check is False
        return subprocess.CompletedProcess(
            command_args, returncode=1, stdout="", stderr=""
        )

    monkeypatch.setattr(subprocess, "run", fake_run)

    result = BranchChaosIncident().run()

    assert result == ""
    assert calls == [
        {
            "command_args": ["false"],
            "capture_output": True,
            "text": True,
            "check": False,
        }
    ]


def test_execute_shell_command_returns_stdout_for_nonzero_exit(monkeypatch):
    def fake_run(command_args, *, capture_output, text, check):
        assert command_args == ["false"]
        assert capture_output is True
        assert text is True
        assert check is False
        return subprocess.CompletedProcess(
            command_args, returncode=1, stdout="partial output\n", stderr="failure\n"
        )

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert BranchChaosIncident().execute_shell_command(["false"]) == "partial output\n"