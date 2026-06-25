from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter


def test_parse_confidence_valid_numeric():
    adapter = BrokenMCPAdapter()
    assert adapter.parse_confidence('0.5') == 0.5
    assert adapter.parse_confidence('1') == 1.0
    assert adapter.parse_confidence('0') == 0.0


def test_parse_confidence_invalid_input_returns_zero_after_fix():
    adapter = BrokenMCPAdapter()
    assert adapter.parse_confidence('invalid') == 0.0
    assert adapter.parse_confidence('') == 0.0
    assert adapter.parse_confidence('   ') == 0.0
