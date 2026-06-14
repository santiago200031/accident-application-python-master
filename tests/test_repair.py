import mcp_servers.sre_tools_server as sre_tools_server

import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 5.0),
    (5, 1, 50.0),
    (0, 5, 0.0),
    (10, 0, 0.0),
    (2, 3, 6.666666666666667),
])
def test_crashy_math(a, b, expected):
    result = sre_tools_server.crashy_math(a, b)
    assert result == expected
