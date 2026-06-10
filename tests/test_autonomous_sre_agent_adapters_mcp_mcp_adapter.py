from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

def test_calculate_risk_zero_checks() -> None:
    adapter = BrokenMCPAdapter()
    incidents = 10
    checks = 0
    risk = adapter.calculate_risk(incidents, checks)
    assert risk == 0.0
