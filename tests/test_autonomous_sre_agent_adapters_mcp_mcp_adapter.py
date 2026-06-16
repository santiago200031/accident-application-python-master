import httpx
from unittest.mock import patch
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter, IncidentSummary, RepairPlan


def test_network_chaos_success():
    adapter = BrokenMCPAdapter()
    with patch.object(BrokenMCPAdapter, 'call_remote_server') as mock_call:
        mock_call.return_value = {'result': 'success'}
        result = adapter.execute('network-chaos')
        assert result == {
            'mode': 'network-chaos',
            'payload': {'result': 'success'}
        }


def test_network_chaos_connect_error():
    adapter = BrokenMCPAdapter()
    with patch.object(BrokenMCPAdapter, 'call_remote_server') as mock_call:
        mock_call.side_effect = httpx.ConnectError('Connection refused')
        result = adapter.execute('network-chaos')
        assert result == {
            'mode': 'network-chaos',
            'payload': {'error': 'Connection refused'}
        }


def test_network_chaos_other_exception():
    adapter = BrokenMCPAdapter()
    with patch.object(BrokenMCPAdapter, 'call_remote_server') as mock_call:
        mock_call.side_effect = ValueError('Something went wrong')
        try:
            adapter.execute('network-chaos')
        except ValueError as e:
            assert str(e) == 'Something went wrong'
        else:
            assert False, 'Expected ValueError'
