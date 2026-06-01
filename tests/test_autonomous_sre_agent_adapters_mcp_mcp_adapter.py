import unittest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

class TestBrokenMCPAdapterCalculateRisk(unittest.TestCase):
    def test_calculate_risk_division_by_zero(self):
        adapter = BrokenMCPAdapter()
        # This test should fail before the fix
        risk = adapter.calculate_risk(incidents=5, checks=0)
        self.assertEqual(risk, 0.0)  # This should pass after the fix

    def test_calculate_risk_valid_input(self):
        adapter = BrokenMCPAdapter()
        risk = adapter.calculate_risk(incidents=10, checks=2)
        self.assertEqual(risk, 5.0)

    def test_calculate_risk_checks_is_one(self):
        adapter = BrokenMCPAdapter()
        risk = adapter.calculate_risk(incidents=5, checks=1)
        self.assertEqual(risk, 5.0)

    def test_calculate_risk_incidents_is_zero(self):
        adapter = BrokenMCPAdapter()
        risk = adapter.calculate_risk(incidents=0, checks=5)
        self.assertEqual(risk, 0.0)
