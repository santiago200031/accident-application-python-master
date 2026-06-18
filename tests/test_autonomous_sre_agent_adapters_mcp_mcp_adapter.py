import pytest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter
from unittest.mock import patch, MagicMock


def test_execute_repair_command_normal_command():
    adapter = BrokenMCPAdapter()
    with patch('autonomous_sre_agent.adapters.mcp.mcp_adapter.subprocess.run') as mock_run:
        mock_result = MagicMock()
        mock_result.stdout = 'hello\n'
        mock_run.return_value = mock_result

        result = adapter.execute_repair_command('echo hello')

        assert result == 'hello\n'
        mock_run.assert_called_once_with(
            ['echo', 'hello'],
            capture_output=True,
            text=True,
            check=False
        )


def test_execute_repair_command_empty_string():
    adapter = BrokenMCPAdapter()
    with patch('autonomous_sre_agent.adapters.mcp.mcp_adapter.subprocess.run') as mock_run:
        result = adapter.execute_repair_command('')
        assert result == ''
        mock_run.assert_not_called()


def test_execute_repair_command_whitespace_only():
    adapter = BrokenMCPAdapter()
    with patch('autonomous_sre_agent.adapters.mcp.mcp_adapter.subprocess.run') as mock_run:
        result = adapter.execute_repair_command('   ')
        assert result == ''
        mock_run.assert_not_called()


def test_execute_repair_command_shell_metacharacters():
    adapter = BrokenMCPAdapter()
    with patch('autonomous_sre_agent.adapters.mcp.mcp_adapter.subprocess.run') as mock_run:
        mock_result = MagicMock()
        mock_result.stdout = 'safe output'
        mock_run.return_value = mock_result

        result = adapter.execute_repair_command('echo hello; rm -rf /')

        assert result == 'safe output'
        # Verify the command was split correctly and shell=True was not used
        mock_run.assert_called_once_with(
            ['echo', 'hello;', 'rm', '-rf', '/'],
            capture_output=True,
            text=True,
            check=False
        )
