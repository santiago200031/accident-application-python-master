from __future__ import annotations

import subprocess

from incident_package.base import Incident


class BranchChaosIncident(Incident):
    mode = "branch-chaos"

    def execute_shell_command(self, command_args: list[str]) -> str:
        if not command_args:
            return ""

        try:
            result = subprocess.run(
                command_args, capture_output=True, text=True
            )
        except (subprocess.CalledProcessError, OSError, ValueError, TypeError):
            return ""

        if result.returncode != 0:
            return ""

        return result.stdout or ""

    def run(self) -> str:
        failing_cmd = ["false"]
        return self.execute_shell_command(failing_cmd)