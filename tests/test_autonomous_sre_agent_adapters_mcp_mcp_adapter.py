from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter


def test_execute_index_error_mode_returns_without_error():
    adapter = BrokenMCPAdapter()
    result = adapter.execute(mode='index-error')
    assert isinstance(result, dict)
    assert result.get('mode') == 'index-error'
    assert 'value' in result
