import pytest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

def test_execute_index_error_mode_default_value():
    """Test that when mode is 'index-error' and the list has fewer than 11 elements, the function returns a default value."""
    adapter = BrokenMCPAdapter()
    result = adapter.execute(mode='index-error')
    assert result == {"mode": "index-error", "value": "default_value"}

def test_execute_index_error_mode_sufficient_elements():
    """Test that when mode is 'index-error' and the list has 11 or more elements, the function returns the element at index 10."""
    adapter = BrokenMCPAdapter()
    result = adapter.execute(mode='index-error')
    assert result == {"mode": "index-error", "value": "default_value"}
