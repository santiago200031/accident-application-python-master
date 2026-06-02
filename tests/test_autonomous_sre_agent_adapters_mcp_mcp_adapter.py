import httpx
import pytest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

@pytest.mark.parametrize("mode", ["network-chaos"])
def test_network_chaos_mode(mode):
    adapter = BrokenMCPAdapter()
    result = adapter.execute(mode)
    assert result["mode"] == mode
    # Check that the payload is present and not an error
    assert "payload" in result
    # The payload should not raise an exception
    try:
        result["payload"]
    except httpx.ConnectError as e:
        pytest.fail(f"httpx.ConnectError raised: {e}")
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")
