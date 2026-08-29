import subprocess
from unittest.mock import patch, MagicMock

import pytest


class TestCommandExecutorService:
    """Regression tests for inc-2026-007: CalledProcessError handling."""

    def test_execute_shell_command_returns_empty_string_on_nonzero_exit(self):
        """
        The fixed behavior is that execute_shell_command catches
        subprocess.CalledProcessError and returns an empty string instead of
        propagating the exception.
        
        Pre-patch code would have raised CalledProcessError when running a
        command that exits with non-zero status (like 'false').
        """
        from incident_package.services.command_executor_service import BranchChaosIncident

        service = BranchChaosIncident()
        # Running "false" always exits with status 1
        result = service.execute_shell_command(["false"])
        assert result == ""

    def test_execute_shell_command_returns_stdout_on_success(self):
        """
        Verify that successful commands still return their stdout.
        """
        from incident_package.services.command_executor_service import BranchChaosIncident

        service = BranchChaosIncident()
        # "echo hello" should succeed and output "hello\n"
        result = service.execute_shell_command(["echo", "hello"])
        assert result == "hello\n"

    def test_execute_shell_command_returns_empty_string_on_file_not_found(self):
        """
        Verify that FileNotFoundError is also caught and returns empty string.
        """
        from incident_package.services.command_executor_service import BranchChaosIncident

        service = BranchChaosIncident()
        # A non-existent command should trigger FileNotFoundError
        result = service.execute_shell_command(["nonexistent_command_xyz_12345"])
        assert result == ""

    def test_run_returns_empty_string_for_failing_command(self):
        """
        The run method uses a failing command and should return empty string,
        not raise an exception.
        
        Pre-patch: this would have raised CalledProcessError.
        Post-patch: returns "".
        """
        from incident_package.services.command_executor_service import BranchChaosIncident

        service = BranchChaosIncident()
        result = service.run()
        assert result == ""

    def test_mode_attribute_is_branch_chaos(self):
        """Verify the mode attribute is correctly set."""
        from incident_package.services.command_executor_service import BranchChaosIncident

        service = BranchChaosIncident()
        assert service.mode == "branch-chaos"