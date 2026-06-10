import pytest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

@pytest.fixture
def broken_mcp_adapter():
    return BrokenMCPAdapter()

def test_calculate_risk_with_zero_checks(broken_mcp_adapter):
    incidents = 10
    checks = 0
    risk = broken_mcp_adapter.calculate_risk(incidents, checks)
    assert risk == 0.0

def test_calculate_risk_with_non_zero_checks(broken_mcp_adapter):
    incidents = 10
    checks = 5
    risk = broken_mcp_adapter.calculate_risk(incidents, checks)
    assert risk == 2.0
