from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

def test_parse_confidence_valid_numeric():
    adapter = BrokenMCPAdapter()
    assert adapter.parse_confidence("0.5") == 0.5
    assert adapter.parse_confidence("1") == 1.0
    assert adapter.parse_confidence("0") == 0.0
    assert adapter.parse_confidence("-0.2") == -0.2

def test_parse_confidence_invalid_returns_zero():
    adapter = BrokenMCPAdapter()
    assert adapter.parse_confidence("not-a-number") == 0.0
    assert adapter.parse_confidence("") == 0.0
    assert adapter.parse_confidence("abc123") == 0.0

def test_parse_confidence_with_whitespace():
    adapter = BrokenMCPAdapter()
    assert adapter.parse_confidence(" 3.14 ") == 3.14
