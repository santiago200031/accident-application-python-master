def test_network_chaos_timeout_failure(mcp_adapter: BrokenMCPAdapter) -> None:
    # This test reproduces the original error by attempting to connect to a non-existent endpoint with a short timeout.
    # Before the fix, this test should fail with a httpx.ConnectError.
    with pytest.raises(httpx.ConnectError):
        mcp_adapter.execute(mode='network-chaos')
