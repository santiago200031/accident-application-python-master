import pytest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

@pytest.mark.parametrize("mode", ["network-chaos"])
def test_execute_network_chaos_mode(mode):
    adapter = BrokenMCPAdapter()
    result = adapter.execute(mode)
    assert result == {"mode": mode}
