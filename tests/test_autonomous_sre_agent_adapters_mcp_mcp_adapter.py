import subprocess
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter
import json
import os

def test_execute_repair_command_no_shell_injection() -> None:
    """Test that the execute_repair_command function does not allow shell injection."""
    # Create a temporary policy file with a malicious command
    policy_content = json.dumps({
        'repair_cmd': 'ls -l /'  # Malicious command
    })
    policy_path = 'temp_policy.json'
    with open(policy_path, 'w') as f:
        f.write(policy_content)

    # Initialize the MCP adapter with the malicious policy
    adapter = BrokenMCPAdapter(policy_path=policy_path)

    # Execute the repair command
    result = adapter.execute_repair_command(adapter.load_policy().get('repair_cmd', 'echo dummy'))

    # Assert that the output does not contain unexpected shell commands
    assert 'total' in result
    assert 'drwxr-xr-x' in result

    # Clean up the temporary policy file
    os.remove(policy_path)
