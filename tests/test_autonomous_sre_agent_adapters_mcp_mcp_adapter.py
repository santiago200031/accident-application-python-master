import autonomous_sre_agent.adapters.mcp.mcp_adapter

class TestMCPAdapterExecuteIndexError(autonomous_sre_agent.adapters.mcp.mcp_adapter.BrokenMCPAdapter):
    def test_execute_index_error_mode(self):
        adapter = autonomous_sre_agent.adapters.mcp.mcp_adapter.BrokenMCPAdapter()
        result = adapter.execute(mode='index-error')
        assert result == {'mode': 'index-error', 'value': 'first'}
