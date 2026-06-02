import autonomous_sre_agent.adapters.mcp.mcp_adapter

class TestMCPAdapter(autonomous_sre_agent.adapters.mcp.mcp_adapter.BrokenMCPAdapter):
    def test_parse_confidence_valid(self):
        policy = {"confidence": "1.0"}
        adapter = autonomous_sre_agent.adapters.mcp.mcp_adapter.BrokenMCPAdapter(policy_path="dummy")
        confidence = adapter.parse_confidence(policy.get('confidence', 'dummy'))
        assert confidence == 1.0

    def test_parse_confidence_invalid(self):
        policy = {"confidence": "not_a_number"}
        adapter = autonomous_sre_agent.adapters.mcp.mcp_adapter.BrokenMCPAdapter(policy_path="dummy")
        confidence = adapter.parse_confidence(policy.get('confidence', 'dummy'))
        assert confidence == 0.0
