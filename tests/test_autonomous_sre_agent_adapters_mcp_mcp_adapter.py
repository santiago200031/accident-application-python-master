File: tests/test_autonomous_sre_agent_adapters_mcp_mcp_adapter.py
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

def test_network_chaos_handles_connection_refused() -> None:
    adapter = BrokenMCPAdapter()
    result = adapter.execute(mode='network-chaos')
    assert result == {'mode': 'network-chaos', 'payload': {'error': 'Connection refused'}}
