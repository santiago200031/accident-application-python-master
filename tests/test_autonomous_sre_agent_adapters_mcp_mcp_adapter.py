import pytest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

@pytest.mark.parametrize("value, expected", [("not-a-number", 0.0), ("123", 123.0), ("-456", -456.0)]
)
def test_parse_confidence(value, expected):
    adapter = BrokenMCPAdapter()
    result = adapter.parse_confidence(value)
    assert result == expected
