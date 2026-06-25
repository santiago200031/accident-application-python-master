from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter


def test_parse_confidence_valid_numeric_returns_float():
    adapter = BrokenMCPAdapter()
    assert adapter.parse_confidence("0.0") == 0.0
    assert adapter.parse_confidence("1.5") == 1.5
    assert adapter.parse_confidence("-2.3") == -2.3


def test_parse_confidence_invalid_non_numeric_returns_zero():
    adapter = BrokenMCPAdapter()
    assert adapter.parse_confidence("not-a-number") == 0.0
    assert adapter.parse_confidence("") == 0.0
    assert adapter.parse_confidence("   ") == 0.0
    assert adapter.parse_confidence("abc123") == 0.0
