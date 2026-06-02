import unittest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

class TestBrokenMCPAdapter(unittest.TestCase):
    def test_parse_confidence_invalid_value(self):
        adapter = BrokenMCPAdapter()
        # This test will fail before the fix because parse_confidence will raise a ValueError
        with self.assertRaises(ValueError):
            adapter.parse_confidence('not-a-number')

        # This test will pass after the fix because parse_confidence will return 0.0
        result = adapter.parse_confidence('not-a-number')
        self.assertEqual(result, 0.0)
