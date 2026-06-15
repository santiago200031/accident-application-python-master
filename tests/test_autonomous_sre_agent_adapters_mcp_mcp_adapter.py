import pytest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

@pytest.fixture
def incidents():
    return 10

@pytest.fixture
def checks():
    return 0

@pytest.fixture
def expected_risk():
    return 0.0

def test_calculate_risk_zero_checks(incidents, checks, expected_risk):
    adapter = BrokenMCPAdapter()
    risk = adapter.calculate_risk(incidents=incidents, checks=checks)
    assert risk == expected_risk

def test_calculate_risk_non_zero_checks(incidents, checks=2, expected_risk=5.0):
    adapter = BrokenMCPAdapter()
    risk = adapter.calculate_risk(incidents=incidents, checks=checks)
    assert risk == expected_risk
