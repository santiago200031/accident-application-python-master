import pytest
from mcp_servers.sre_tools_server import crashy_math


def test_crashy_math_valid_denominator():
    assert crashy_math(10, 2) == 50.0

def test_crashy_math_zero_denominator():
    assert crashy_math(10, 0) == 0.0
