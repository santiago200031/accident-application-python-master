import subprocess

from incident_package.services import command_executor_service


def test_run_handles_nonzero_false_command_without_raising(monkeypatch):
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
        result = subprocess.CompletedProcess(
            args=command_args,
            returncode=1,
            stdout="",
            stderr="",
        )
        if check and result.returncode != 0:
            raise subprocess.CalledProcessError(
                result.returncode,
                result.args,
                output=result.stdout,
                stderr=result.stderr,
            )
        return result

    monkeypatch.setattr(
        command_executor_service.subprocess,
        "run",
        fake_run,
    )

    incident = command_executor_service.BranchChaosIncident()

    assert incident.run() == ""
    assert calls == [
        {
            "command_args": ["false"],
            "capture_output": True,
            "text": True,
            "check": False,
        }
    ]