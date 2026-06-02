import httpx
import pytest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

@pytest.fixture
def mcp_adapter():
    return BrokenMCPAdapter()

def test_network_chaos_handles_connection_refusal(mcp_adapter):
    result = mcp_adapter.execute('network-chaos')
    assert result == {'mode': 'network-chaos', 'payload': {'error': 'Connection refused'}}
