from __future__ import annotations

import pytest

from incident_package.utils.data_parser import BadCastIncident

class TestBadCastIncidentRegression:
    """Regression tests for incident inc-2026-002.

    Pre-patch behavior: `parse_float_setting` performed an unchecked `float()`
    cast, raising `ValueError: could not convert string to float: 'not-a-number'`
    when given non-numeric input.

    Patched behavior: invalid input yields a `0.0` default instead of raising.
    """

    def test_parse_float_setting_returns_zero_for_non_numeric_string(self) -> None:
        """The exact incident input must not raise and must return 0.0.

        This test FAILS against the pre-patch code because `float('not-a-number')`
        raises `ValueError`.
        """
        incident = BadCastIncident()
        assert incident.parse_float_setting("not-a-number") == 0.0

    def test_run_does_not_raise_on_bad_cast_mode(self) -> None:
        """`run()` reproduces the incident scenario and must return 0.0.

        Pre-patch, `run()` propagated the `ValueError` from the unchecked cast.
        """
        incident = BadCastIncident()
        assert incident.run() == 0.0

    def test_parse_float_setting_handles_empty_string(self) -> None:
        """Empty string is not a valid numeric literal and must default to 0.0."""
        incident = BadCastIncident()
        assert incident.parse_float_setting("") == 0.0

    def test_parse_float_setting_handles_none_input(self) -> None:
        """`None` triggers a `TypeError` in `float()`; patched code catches it."""
        incident = BadCastIncident()
        assert incident.parse_float_setting(None) == 0.0  # type: ignore[arg-type]

    def test_parse_float_setting_preserves_valid_integer_string(self) -> None:
        """Valid numeric strings must still parse correctly after the fix."""
        incident = BadCastIncident()
        assert incident.parse_float_setting("42") == 42.0

    def test_parse_float_setting_preserves_valid_float_string(self) -> None:
        """Valid float strings must still parse correctly after the fix."""
        incident = BadCastIncident()
        assert incident.parse_float_setting("3.14") == pytest.approx(3.14)

    def test_parse_float_setting_preserves_negative_and_scientific(self) -> None:
        """Negative and scientific-notation strings remain valid inputs."""
        incident = BadCastIncident()
        assert incident.parse_float_setting("-1.5") == -1.5
        assert incident.parse_float_setting("1e3") == 1000.0

    def test_parse_float_setting_handles_whitespace_padded_numeric(self) -> None:
        """`float()` tolerates surrounding whitespace; the fix must not regress that."""
        incident = BadCastIncident()
        assert incident.parse_float_setting("  12.5  ") == 12.5

    def test_parse_float_setting_returns_float_type(self) -> None:
        """The return type must be `float` for both valid and invalid inputs."""
        incident = BadCastIncident()
        assert isinstance(incident.parse_float_setting("not-a-number"), float)
        assert isinstance(incident.parse_float_setting("7"), float)

    def test_incident_mode_matches_bad_cast(self) -> None:
        """Sanity check that the incident class is wired to the expected mode."""
        assert BadCastIncident.mode == "bad-cast"