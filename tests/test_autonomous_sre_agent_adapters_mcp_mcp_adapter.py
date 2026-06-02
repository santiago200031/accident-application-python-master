import autonomous_sre_agent.adapters.mcp.mcp_adapter as mcp_adapter
import pytest

@pytest.fixture
def mcp_adapter_instance():
    return mcp_adapter.BrokenMCPAdapter()

def test_execute_none_dereference_summary_is_none():
    # Arrange
    adapter = mcp_adapter.BrokenMCPAdapter()
    # Act
    result = adapter.execute(mode='none-dereference')
    # Assert
    assert result['mode'] == 'none-dereference'
    assert result['critical_count'] == 0
