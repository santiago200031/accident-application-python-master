import pytest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

class TestBrokenMCPAdapter(object):
    def test_calculate_risk_with_zero_checks(self):
        adapter = BrokenMCPAdapter()
        incidents = 10
        checks = 0
        risk = adapter.calculate_risk(incidents, checks)
        assert risk == 0.0

    def test_calculate_risk_with_non_zero_checks(self):
        adapter = BrokenMCPAdapter()
        incidents = 10
        checks = 5
        risk = adapter.calculate_risk(incidents, checks)
        assert risk == 2.0
