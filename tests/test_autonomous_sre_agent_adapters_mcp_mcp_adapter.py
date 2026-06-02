import subprocess
import pytest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

@pytest.fixture
def mcp_adapter():
    return BrokenMCPAdapter()

def test_execute_repair_command_no_shell_injection(mcp_adapter):
    # Arrange
    policy = {
        'repair_cmd': 'echo hello world; whoami'  # Command with potential injection
    }
    mcp_adapter.load_policy = lambda: policy

    # Act
    output = mcp_adapter.execute_repair_command(policy['repair_cmd'])

    # Assert
    assert 'hello world' in output
    assert 'whoami' not in output  # Ensure shell injection didn't occur
