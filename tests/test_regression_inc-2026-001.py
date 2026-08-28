from __future__ import annotations

import pytest

from incident_package.utils.math_calculator import DivideByZeroIncident


def test_divide_two_numbers_with_zero_denominator_returns_zero() -> None:
    incident = DivideByZeroIncident()

    result = incident.divide_two_numbers(5.0, 0.0)

    assert result == 0.0


def test_run_reproduces_original_incident_scenario_without_zero_division_error() -> None:
    incident = DivideByZeroIncident()

    result = incident.run()

    assert result == 0.0


def test_nonzero_denominator_still_performs_normal_division() -> None:
    incident = DivideByZeroIncident()

    result = incident.divide_two_numbers(10.0, 2.0)

    assert result == 5.0


def test_incident_mode_is_divide_by_zero() -> None:
    assert DivideByZeroIncident.mode == "divide-by-zero"