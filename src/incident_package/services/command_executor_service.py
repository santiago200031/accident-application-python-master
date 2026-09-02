from __future__ import annotations

import subprocess

from incident_package.base import Incident

class BranchChaosIncident(Incident):
    mode = "branch-chaos"

    def execute_shell_command(self, command_args: list[str]) -> str:
        try:
            result = subprocess.run(
                command_args, capture_output=True, text=True, check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            # Handle the error gracefully by returning a safe default value
            return "Command failed with exit code 1"

    def run(self) -> str:
        failing_cmd = ["false"]
        return self.execute_shell_command(failing_cmd)