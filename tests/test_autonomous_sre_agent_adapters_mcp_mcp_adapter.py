import autonomous_sre_agent.adapters.mcp.mcp_adapter as mcp_adapter

import pytest

@pytest.mark.parametrize(
    "incidents, checks, expected_risk",
    [ (10, 2, 5.0), (5, 1, 5.0), (0, 5, 0.0), (10, 0, 0.0), (0, 0, 0.0) ]
)
def test_calculate_risk(incidents, checks, expected_risk):
    adapter = mcp_adapter.McpAdapter()
    risk = adapter.calculate_risk(incidents, checks)
    assert risk == expected_risk
