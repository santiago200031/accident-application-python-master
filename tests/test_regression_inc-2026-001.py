import sys
from pathlib import Path

# Ensure src directory is on the path for imports.
_SRC_ROOT = Path(__file__).resolve().parent.parent / "src"
if str(_SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(_SRC_ROOT))

import pytest

from incident_package.utils.math_calculator import DivideByZeroIncident


class TestDivideByZeroIncident:
    """Regression tests for the patched math_calculator module."""

    def test_mode_attribute(self):
        assert DivideByZeroIncident().mode == "divide-by-zero"

    def test_divide_two_numbers_zero_denom(self):
        incident = DivideByZeroIncident()
        assert incident.divide_two_numbers(10.0, 0.0) == 0.0

    def test_divide_two_numbers_normal(self):
        incident = DivideByZeroIncident()
        assert incident.divide_two_numbers(10.0, 2.0) == 5.0

    def test_run_with_zero_total_count(self):
        incident = DivideByZeroIncident()
        assert incident.run() == 0.0