import pytest

from incident_package.utils.data_parser import BadCastIncident


class TestBadCastIncident:
    def test_parse_float_setting_with_valid_number(self):
        """Test that valid numeric strings are parsed correctly."""
        incident = BadCastIncident()
        result = incident.parse_float_setting("3.14")
        assert result == 3.14

    def test_parse_float_setting_with_integer_string(self):
        """Test that integer strings are parsed to float."""
        incident = BadCastIncident()
        result = incident.parse_float_setting("42")
        assert result == 42.0

    def test_parse_float_setting_with_negative_number(self):
        """Test that negative numbers are parsed correctly."""
        incident = BadCastIncident()
        result = incident.parse_float_setting("-1.5")
        assert result == -1.5

    def test_parse_float_setting_with_invalid_string_returns_zero(self):
        """
        Test the fixed behavior: invalid strings should return 0.0 instead of raising ValueError.
        
        This test would FAIL against pre-patch code that didn't have try/except handling,
        as it would raise ValueError when trying to convert 'not-a-number' to float.
        """
        incident = BadCastIncident()
        result = incident.parse_float_setting("not-a-number")
        assert result == 0.0

    def test_parse_float_setting_with_empty_string_returns_zero(self):
        """Test that empty strings return 0.0."""
        incident = BadCastIncident()
        result = incident.parse_float_setting("")
        assert result == 0.0

    def test_parse_float_setting_with_none_returns_zero(self):
        """Test that None input returns 0.0 (TypeError handling)."""
        incident = BadCastIncident()
        result = incident.parse_float_setting(None)
        assert result == 0.0

    def test_run_method_with_invalid_input_returns_zero(self):
        """
        Test the run method with the original incident scenario.
        
        This reproduces the exact incident scenario where 'not-a-number' was passed,
        which previously caused ValueError: could not convert string to float: 'not-a-number'.
        The fixed behavior should return 0.0 instead of raising an exception.
        """
        incident = BadCastIncident()
        result = incident.run()
        assert result == 0.0

    def test_run_method_does_not_raise_value_error(self):
        """
        Explicitly verify that no ValueError is raised for the original incident scenario.
        
        This test would FAIL against pre-patch code because it would raise ValueError
        when attempting to convert 'not-a-number' to float without proper exception handling.
        """
        incident = BadCastIncident()
        # Should not raise any exception
        result = incident.run()
        assert isinstance(result, float)