from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter


def test_calculate_risk_normal_case():
    adapter = BrokenMCPAdapter()
    result = adapter.calculate_risk(incidents=10, checks=2)
    assert result == 5.0


def test_calculate_risk_zero_checks_returns_zero():
    adapter = BrokenMCPAdapter()
    result = adapter.calculate_risk(incidents=5, checks=0)
    assert result == 0.0


def test_calculate_risk_zero_incidents_and_checks():
    adapter = BrokenMCPAdapter()
    result = adapter.calculate_risk(incidents=0, checks=0)
    assert result == 0.0


def test_calculate_risk_zero_incidents_nonzero_checks():
    adapter = BrokenMCPAdapter()
    result = adapter.calculate_risk(incidents=0, checks=10)
    assert result == 0.0
