import subprocess

import pytest

from incident_package.services.command_executor_service import BranchChaosIncident


def test_run_handles_expected_failure_from_false_without_raising(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: dict[str, object] = {}

    def fake_run(
        command_args: list[str],
        *,
        capture_output: bool,
        text: bool,
        check: bool,
    ) -> subprocess.CompletedProcess[str]:
        calls.update(
            command_args=command_args,
            capture_output=capture_output,
            text=text,
            check=check,
        )
        if check:
            raise subprocess.CalledProcessError(
                returncode=1,
                cmd=command_args,
                stdout="",
                stderr="",
            )
        return subprocess.CompletedProcess(
            args=command_args,
            returncode=1,
            stdout="",
            stderr="",
        )

    monkeypatch.setattr(subprocess, "run", fake_run)

    result = BranchChaosIncident().run()

    assert result == ""
    assert calls == {
        "command_args": ["false"],
        "capture_output": True,
        "text": True,
        "check": False,
    }