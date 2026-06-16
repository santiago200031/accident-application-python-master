import pytest
from unittest.mock import patch, MagicMock
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter


def test_execute_none_dereference_returns_zero_when_aggregate_returns_none():
    """Test that execute returns critical_count=0 when aggregate_incidents returns None in none-dereference mode."""
    adapter = BrokenMCPAdapter(policy_path='/tmp/asre-nonexistent/__does_not_exist__.json')
    with patch.object(adapter, 'load_policy', return_value={}):
        with patch.object(adapter, 'aggregate_incidents', return_value=None) as mock_agg:
            result = adapter.execute(mode='none-dereference')
            mock_agg.assert_called_once_with([{'severity': 'LOW', 'id': 1}])
            assert result == {'mode': 'none-dereference', 'critical_count': 0}


def test_execute_none_dereference_preserves_existing_behavior_when_aggregate_returns_value():
    """Test that execute returns correct critical_count when aggregate_incidents returns a value in none-dereference mode."""
    adapter = BrokenMCPAdapter(policy_path='/tmp/asre-nonexistent/__does_not_exist__.json')
    with patch.object(adapter, 'load_policy', return_value={}):
        with patch.object(adapter, 'aggregate_incidents', return_value={'count': 42}) as mock_agg:
            result = adapter.execute(mode='none-dereference')
            mock_agg.assert_called_once_with([{'severity': 'LOW', 'id': 1}])
            assert result == {'mode': 'none-dereference', 'critical_count': 42}
