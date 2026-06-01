import unittest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

class TestBrokenMCPAdapterCalculateRisk(unittest.TestCase):
    def test_calculate_risk_division_by_zero(self):
        adapter = BrokenMCPAdapter()
        # This test should fail before the fix
        risk = adapter.calculate_risk(incidents=5, checks=0)
        self.assertEqual(risk, 0.0)

    def test_calculate_risk_valid_division(self):
        adapter = BrokenMCPAdapter()
        # This test should pass before and after the fix
        risk = adapter.calculate_risk(incidents=5, checks=2)
        self.assertEqual(risk, 2.5)

    def test_calculate_risk_checks_is_one(self):
        adapter = BrokenMCPAdapter()
        risk = adapter.calculate_risk(incidents=10, checks=1)
        self.assertEqual(risk, 10.0)
