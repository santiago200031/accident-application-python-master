import pytest
from mcp_servers.sre_tools_server import calculate_risk


def test_calculate_risk_normal():
    assert calculate_risk(10, 2) == 5.0

def test_calculate_risk_zero_denominator():
    assert calculate_risk(10, 0) == 0
