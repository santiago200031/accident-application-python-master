import subprocess

import incident_package.services.command_executor_service as command_executor_service


def test_branch_chaos_false_command_returns_controlled_empty_result(monkeypatch):
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
        if check:
            raise subprocess.CalledProcessError(
                1,
                command_args,
                output="",
                stderr="intentional failure",
            )
        return subprocess.CompletedProcess(
            command_args,
            returncode=1,
            stdout="",
            stderr="intentional failure",
        )

    monkeypatch.setattr(command_executor_service.subprocess, "run", fake_run)

    result = command_executor_service.BranchChaosIncident().run()

    assert result == ""
    assert calls == [
        {
            "command_args": ["false"],
            "capture_output": True,
            "text": True,
            "check": False,
        }
    ]