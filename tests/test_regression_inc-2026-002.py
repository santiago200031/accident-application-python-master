from __future__ import annotations

import sys
from pathlib import Path

# Ensure the project root is on sys.path so that incident_package can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from incident_package.utils.data_parser import BadCastIncident


def test_parse_float_setting_returns_zero_for_invalid_string():
    """
    Regression test for inc-2026-002.
    
    The original bug was that passing a non-numeric string like 'not-a-number' 
    to float() would raise a ValueError, which propagated up and crashed the application.
    
    The fix ensures that parse_float_setting catches the ValueError and returns 0.0 instead.
    """
    incident = BadCastIncident()
    
    # This specific input caused the original crash: "could not convert string to float: 'not-a-number'"
    result = incident.parse_float_setting("not-a-number")
    
    assert result == 0.0, (
        f"Expected parse_float_setting('not-a-number') to return 0.0 for invalid input, "
        f"but got {result!r}"
    )


def test_parse_float_setting_returns_correct_value_for_valid_string():
    """
    Ensure that valid numeric strings are still parsed correctly after the fix.
    This prevents over-correction where all inputs might return 0.0.
    """
    incident = BadCastIncident()
    
    # Valid float string
    assert incident.parse_float_setting("3.14") == 3.14
    
    # Valid int-as-string
    assert incident.parse_float_setting("42") == 42.0
    
    # Negative number
    assert incident.parse_float_setting("-5.5") == -5.5


def test_run_method_does_not_raise_for_invalid_input():
    """
    Integration-level regression test for inc-2026-002.
    
    The run() method internally calls parse_float_setting with 'not-a-number'.
    Before the fix, this would raise ValueError and crash.
    After the fix, it should return 0.0 without raising any exception.
    """
    incident = BadCastIncident()
    
    # This call previously raised:
    # ValueError: could not convert string to float: 'not-a-number'
    result = incident.run()
    
    assert result == 0.0, (
        f"Expected run() to return 0.0 when internal setting is invalid, "
        f"but got {result!r}"
    )