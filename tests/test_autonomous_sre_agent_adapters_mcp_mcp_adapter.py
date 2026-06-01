import pytest
import json
from unittest.mock import MagicMock, patch
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

@pytest.fixture
def setup_adapter():
    # Mock necessary dependencies for initialization
    with patch('autonomous_sre_agent.adapters.mcp.mcp_adapter.Path') as MockPath:
        MockPath.return_value.read_text.return_value = "{}"
        adapter = BrokenMCPAdapter(policy_path='dummy_policy.json')
        # Manually set up the instance state if needed, but for this test, initialization is enough.
        return adapter

class TestBrokenMCPAdapterRiskCalculation:

    @patch('autonomous_sre_agent.adapters.mcp.mcp_adapter.httpx')
    def test_calculate_risk_normal_division(self, mock_httpx, setup_adapter): 
        # Test case where both incidents and checks are non-zero
        adapter = setup_adapter
        incidents = 10
        checks = 5
        expected_risk = 2.0
        actual_risk = adapter.calculate_risk(incidents=incidents, checks=checks)
        assert actual_risk == pytest.approx(expected_risk)

    @patch('autonomous_sre_agent.adapters.mcp.mcp_adapter.httpx')
    def test_calculate_risk_zero_checks_prevents_division_by_zero(self, mock_httpx, setup_adapter): 
        # Test case that previously caused ZeroDivisionError (checks=0)
        # Expected behavior after fix: returns 0
        adapter = setup_adapter
        incidents = 10
        checks = 0
        expected_risk = 0.0
        actual_risk = adapter.calculate_risk(incidents=incidents, checks=checks)
        assert actual_risk == pytest.approx(expected_risk)

    @patch('autonomous_sre_agent.adapters.mcp.mcp_adapter.httpx')
    def test_calculate_risk_zero_incidents_and_checks(self, mock_httpx, setup_adapter): 
        # Test case where both are zero
        adapter = setup_adapter
        incidents = 0
        checks = 0
        expected_risk = 0.0
        actual_risk = adapter.calculate_risk(incidents=incidents, checks=checks)
        assert actual_risk == pytest.approx(expected_risk)

    @patch('autonomous_sre_agent.adapters.mcp.mcp_adapter.httpx')
    def test_calculate_risk_zero_incidents_non_zero_checks(self, mock_httpx, setup_adapter):
        # Test case where incidents=0, checks>0
        adapter = setup_adapter
        incidents = 0
        checks = 5
        expected_risk = 0.0
        actual_risk = adapter.calculate_risk(incidents=incidents, checks=checks)
        assert actual_risk == pytest.approx(expected_risk)
