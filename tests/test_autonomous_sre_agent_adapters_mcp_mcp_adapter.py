import autonomous_sre_agent.adapters.mcp.mcp_adapter as mcp_adapter
import pytest

@pytest.mark.parametrize(
    "mode",
    ["index-error"],
)
def test_execute_index_error_mode(mode):
    adapter = mcp_adapter.BrokenMCPAdapter()
    result = adapter.execute(mode=mode)
    assert result == {"mode": mode, "value": "first"}

@pytest.mark.parametrize(
    "mode",
    ["divide-by-zero", "bad-cast", "missing-file", "network-chaos", "none-dereference", "command-injection", "branch-chaos", "remediation-workflow", "default"],
)
def test_execute_other_modes(mode):
    adapter = mcp_adapter.BrokenMCPAdapter()
    result = adapter.execute(mode=mode)
    assert "mode" in result
    assert "value" not in result
