import pytest
from mcp_servers.sre_tools_server import crashy_math


def test_crashy_math_b_is_zero():
    assert crashy_math(10, 0) == 0

def test_crashy_math_b_is_not_zero():
    assert crashy_math(10, 2) == 50
