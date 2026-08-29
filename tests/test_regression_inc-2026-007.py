import subprocess
from unittest.mock import patch

from incident_package.services.command_executor_service import BranchChaosIncident


def test_branch_chaos_false_command_is_recorded_without_raising():
    def controlled_false(command_args, *, capture_output, text, check):
        assert command_args == ["false"]
        assert capture_output is True
        assert text is True
        assert check is False
        return subprocess.CompletedProcess(
            args=command_args,
            returncode=1,
            stdout="",
            stderr="intentional chaos command failure",
        )

    with patch(
        "incident_package.services.command_executor_service.subprocess.run",
        side_effect=controlled_false,
    ):
        result = BranchChaosIncident().run()

    assert result == "intentional chaos command failure"