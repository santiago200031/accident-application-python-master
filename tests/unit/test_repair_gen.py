import pytest
from unittest.mock import patch

from incident_package.utils.math_calculator import DivideByZeroIncident

class TestDivideByZeroIncident:
    """Regression tests for incident inc-2026-001: ZeroDivisionError fix."""

    @pytest.fixture
    def incident(self):
        return DivideByZeroIncident()

    def test_divide_two_numbers_normal_case(self, incident):
        """Test normal division returns expected result."""
        result = incident.divide_two_numbers(10.0, 2.0)
        assert result == 5.0

    def test_divide_two_numbers_zero_denominator_raises_value_error(self, incident):
        """Regression test: Verify ValueError is raised instead of ZeroDivisionError."""
        with pytest.raises(ValueError, match="Divisor must not be zero"):
            incident.divide_two_numbers(5.0, 0.0)

    def test_divide_two_numbers_negative_denominator(self, incident):
        """Test division with negative denominator."""
        result = incident.divide_two_numbers(10.0, -2.0)
        assert result == -5.0

    def test_divide_two_numbers_zero_numerator(self, incident):
        """Test division with zero numerator."""
        result = incident.divide_two_numbers(0.0, 5.0)
        assert result == 0.0

    def test_run_method_raises_value_error(self, incident):
        """Regression test: Verify run() raises ValueError instead of ZeroDivisionError."""
        with pytest.raises(ValueError, match="Divisor must not be zero"):
            incident.run()

    def test_divide_two_numbers_large_numbers(self, incident):
        """Test division with large numbers."""
        result = incident.divide_two_numbers(1e10, 1e5)
        assert result == pytest.approx(1e5)

    def test_divide_two_numbers_decimal_numbers(self, incident):
        """Test division with decimal numbers."""
        result = incident.divide_two_numbers(7.5, 2.5)
        assert result == pytest.approx(3.0)