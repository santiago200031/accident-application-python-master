import sys as _sys
import os as _os
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "src"))

import unittest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

class TestBrokenMCPAdapter(unittest.TestCase):
    def test_calculate_risk_with_zero_checks(self):
        adapter = BrokenMCPAdapter()
        risk = adapter.calculate_risk(incidents=5, checks=0)
        self.assertEqual(risk, 0.0)

    def test_calculate_risk_with_non_zero_checks(self):
        adapter = BrokenMCPAdapter()
        risk = adapter.calculate_risk(incidents=5, checks=2)
        self.assertEqual(risk, 2.5)
