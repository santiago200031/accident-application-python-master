from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter
from unittest.mock import patch, MagicMock

def test_execute_repair_command_normal():
    with patch('autonomous_sre_agent.adapters.mcp.mcp_adapter.shlex.split') as mock_split, \
         patch('autonomous_sre_agent.adapters.mcp.mcp_adapter.subprocess.run') as mock_run:
        mock_split.return_value = ['printf', 'hello']
        mock_result = MagicMock()
        mock_result.stdout = 'hello'
        mock_run.return_value = mock_result

        adapter = BrokenMCPAdapter()
        result = adapter.execute_repair_command('printf hello')

        mock_split.assert_called_once_with('printf hello')
        mock_run.assert_called_once_with(['printf', 'hello'], capture_output=True, text=True)
        assert result == 'hello'

def test_execute_repair_command_command_injection_safe():
    with patch('autonomous_sre_agent.adapters.mcp.mcp_adapter.shlex.split') as mock_split, \
         patch('autonomous_sre_agent.adapters.mcp.mcp_adapter.subprocess.run') as mock_run:
        command = 'printf hello; rm -rf /'
        mock_split.return_value = ['printf', 'hello;', 'rm', '-rf', '/']
        mock_result = MagicMock()
        mock_result.stdout = 'hello'
        mock_run.return_value = mock_result

        adapter = BrokenMCPAdapter()
        result = adapter.execute_repair_command(command)

        mock_split.assert_called_once_with(command)
        mock_run.assert_called_once_with(
            ['printf', 'hello;', 'rm', '-rf', '/'],
            capture_output=True,
            text=True
        )
        assert result == 'hello'
