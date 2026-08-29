from __future__ import annotations

import subprocess

from incident_package.base import Incident

class BranchChaosIncident(Incident):
    mode = "branch-chaos"

    def execute_shell_command(self, command_args: list[str]) -> str:
        result = subprocess.run(
            command_args, capture_output=True, text=True
        )
        if result.returncode != 0:
            # Handle non-zero exit status gracefully
            return "Command failed with exit code: {}".format(result.returncode)
        else:
            return result.stdout

    def run(self) -> str:
        failing_cmd = ["false"]
        return self.execute_shell_command(failing_cmd)