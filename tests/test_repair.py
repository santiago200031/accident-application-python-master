import mcp_servers.sre_tools_server as sre_tools_server

def test_calculate_risk_normal():
    result = sre_tools_server.calculate_risk(total_requests=100, total_failures=10)
    assert result == 10.0

def test_calculate_risk_zero_requests():
    result = sre_tools_server.calculate_risk(total_requests=0, total_failures=10)
    assert result == 0.0

def test_calculate_risk_zero_failures():
    result = sre_tools_server.calculate_risk(total_requests=100, total_failures=0)
    assert result == 0.0
