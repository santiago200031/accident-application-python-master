import autonomous_sre_agent.adapters.mcp.mcp_adapter as mcp_adapter
import pytest

@pytest.mark.parametrize(
    "incidents, checks, expected_risk",
    [ (10, 5, 2.0), (5, 2, 2.5), (0, 1, 0.0), (10, 0, 0.0) ]
)
def test_calculate_risk(incidents, checks, expected_risk):
    adapter = mcp_adapter.BrokenMCPAdapter()
    risk = adapter.calculate_risk(incidents, checks)
    assert risk == expected_risk


def test_calculate_risk_zero_checks():
    adapter = mcp_adapter.BrokenMCPAdapter()
    risk = adapter.calculate_risk(10, 0)
    assert risk == 0.0
