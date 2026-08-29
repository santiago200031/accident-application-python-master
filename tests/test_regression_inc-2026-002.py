from __future__ import annotations

import pytest

from incident_package.utils.data_parser import BadCastIncident


class TestBadCastIncident:
    def test_run_returns_zero_for_non_numeric_string(self) -> None:
        """Regression for inc-2026-002.

        The original code raised ``ValueError: could not convert string to float``
        when feeding a non-numeric string into the float cast path. After the
        fix, ``run()`` must return ``0.0`` instead of propagating the exception.
        """
        incident = BadCastIncident()
        result = incident.run()

        assert isinstance(result, float)
        assert result == 0.0

    def test_parse_float_setting_returns_zero_for_non_numeric_string(self) -> None:
        """Directly exercise the guarded cast with the exact offending input."""
        incident = BadCastIncident()
        result = incident.parse_float_setting("not-a-number")

        assert isinstance(result, float)
        assert result == 0.0

    def test_parse_float_setting_returns_zero_for_empty_string(self) -> None:
        """Empty strings also fail ``float()`` and must be handled gracefully."""
        incident = BadCastIncident()
        result = incident.parse_float_setting("")

        assert isinstance(result, float)
        assert result == 0.0

    def test_parse_float_setting_returns_zero_for_none(self) -> None:
        """``TypeError`` path: ``None`` is not convertible to float."""
        incident = BadCastIncident()
        result = incident.parse_float_setting(None)  # type: ignore[arg-type]

        assert isinstance(result, float)
        assert result == 0.0

    def test_parse_float_setting_parses_valid_numeric_string(self) -> None:
        """Valid numeric strings must still be parsed correctly."""
        incident = BadCastIncident()
        assert incident.parse_float_setting("3.14") == pytest.approx(3.14)
        assert incident.parse_float_setting("-2") == -2.0
        assert incident.parse_float_setting("0") == 0.0

    def test_parse_float_setting_parses_integer_string(self) -> None:
        """Integer strings should be converted to float."""
        incident = BadCastIncident()
        result = incident.parse_float_setting("42")

        assert isinstance(result, float)
        assert result == 42.0