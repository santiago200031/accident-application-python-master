import pytest
from mcp_servers.sre_tools_server import calculate_risk


def test_calculate_risk_with_failures():
    total_requests = 100
    total_failures = 10
    risk = calculate_risk(total_requests, total_failures)
    assert risk == 0.1

def test_calculate_risk_no_requests():
    total_requests = 0
    total_failures = 5
    risk = calculate_risk(total_requests, total_failures)
    assert risk == 0.0

def test_calculate_risk_no_failures():
    total_requests = 50
    total_failures = 0
    risk = calculate_risk(total_requests, total_failures)
    assert risk == 0.0
