import subprocess
from unittest.mock import patch, MagicMock

import pytest


class TestCommandExecutorService:
    """Regression tests for inc-2026-007: CalledProcessError handling."""

    def test_execute_shell_command_returns_stdout_on_success(self):
        """Test that successful commands return their stdout."""
        from incident_package.services.command_executor_service import BranchChaosIncident

        service = BranchChaosIncident()
        result = service.execute_shell_command(["echo", "hello"])
        assert result == "hello\n"

    def test_execute_shell_command_returns_empty_string_on_failure(self):
        """Test that failing commands return empty string instead of raising."""
        from incident_package.services.command_executor_service import BranchChaosIncident

        service = BranchChaosIncident()
        # This would raise CalledProcessError in pre-patch code
        result = service.execute_shell_command(["false"])
        assert result == ""

    def test_execute_shell_command_returns_empty_string_on_nonzero_exit(self):
        """Test that non-zero exit codes are handled gracefully."""
        from incident_package.services.command_executor_service import BranchChaosIncident

        service = BranchChaosIncident()
        # exit code 1 should not raise an exception
        result = service.execute_shell_command(["sh", "-c", "exit 1"])
        assert result == ""

    def test_run_returns_empty_string_for_failing_command(self):
        """Test that run method handles failing commands without raising."""
        from incident_package.services.command_executor_service import BranchChaosIncident

        service = BranchChaosIncident()
        # Pre-patch code would raise CalledProcessError here
        result = service.run()
        assert result == ""

    def test_execute_shell_command_captures_stderr_on_failure(self):
        """Test that stderr is captured but not propagated as exception."""
        from incident_package.services.command_executor_service import BranchChaosIncident

        service = BranchChaosIncident()
        # Command that writes to stderr and exits non-zero
        result = service.execute_shell_command(["sh", "-c", "echo error >&2; exit 1"])
        assert result == ""

    def test_execute_shell_command_with_valid_command_returns_output(self):
        """Test that valid commands still return their output correctly."""
        from incident_package.services.command_executor_service import BranchChaosIncident

        service = BranchChaosIncident()
        result = service.execute_shell_command(["echo", "test"])
        assert result == "test\n"

    def test_execute_shell_command_handles_multiple_arguments(self):
        """Test that commands with multiple arguments work correctly."""
        from incident_package.services.command_executor_service import BranchChaosIncident

        service = BranchChaosIncident()
        result = service.execute_shell_command(["echo", "arg1", "arg2", "arg3"])
        assert result == "arg1 arg2 arg3\n"