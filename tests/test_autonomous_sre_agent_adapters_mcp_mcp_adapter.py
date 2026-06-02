import httpx
import pytest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

@pytest.fixture
def mcp_adapter():
    return BrokenMCPAdapter()

def test_network_chaos_success(mcp_adapter):
    result = mcp_adapter.execute('network-chaos')
    assert result['mode'] == 'network-chaos'
    assert 'payload' in result
    # The payload should not raise an exception anymore due to the timeout increase.
    # We just check that it exists.
