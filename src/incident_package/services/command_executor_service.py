from __future__ import annotations

import subprocess

class Incident:
    pass

class BranchChaosIncident(Incident):
    mode = "branch-chaos"

    def execute_shell_command(self, command_args: list[str]) -> str:
        try:
            result = subprocess.run(
                command_args, capture_output=True, text=True, check=True
            )
            return result.stdout
        except subprocess.CalledProcessError:
            # Handle non-zero exit status gracefully by returning an empty string
            return ""

    def run(self) -> str:
        failing_cmd = ["false"]
        return self.execute_shell_command(failing_cmd)