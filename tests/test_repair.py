import pytest
from mcp_servers.sre_tools_server import calculate_risk

def test_calculate_risk_normal():
    data = {'total_failures': 5, 'total_requests': 100}
    risk = calculate_risk(data)
    assert risk == 0.05

def test_calculate_risk_zero_requests():
    data = {'total_failures': 5, 'total_requests': 0}
    risk = calculate_risk(data)
    assert risk == 0.0

def test_calculate_risk_zero_failures():
    data = {'total_failures': 0, 'total_requests': 100}
    risk = calculate_risk(data)
    assert risk == 0.0
