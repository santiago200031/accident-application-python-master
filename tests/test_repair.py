import pytest
from mcp_servers.sre_tools_server import calculate_risk


def test_calculate_risk_empty_data():
    data = []
    result = calculate_risk(data)
    assert result == 0

def test_calculate_risk_valid_data():
    data = [{'risk': 1}, {'risk': 2}, {'risk': 3}]
    result = calculate_risk(data)
    assert result == 6
