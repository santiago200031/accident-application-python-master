import pytest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter
import os

def test_load_policy_file_not_found():
    # Arrange
    with open('config/policy.json', 'w') as f:
        pass  # Create an empty policy.json to simulate missing file
    adapter = BrokenMCPAdapter(policy_path='config/policy.json')

    # Act
    policy = adapter.load_policy()

    # Assert
    assert "default_policy.json" in policy
    # Clean up the created file
    os.remove('config/policy.json')
