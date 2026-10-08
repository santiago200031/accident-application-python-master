import pytest

from incident_package.calculator import calculate_rate


def test_calculate_rate_returns_zero_for_zero_denominator():
    assert calculate_rate(42, 0) == 0.0


@pytest.mark.parametrize(
    ("numerator", "denominator", "expected"),
    [
        (10, 2, 5.0),
        (7, -2, -3.5),
        (0, 5, 0.0),
    ],
)
def test_calculate_rate_divides_nonzero_denominators(numerator, denominator, expected):
    assert calculate_rate(numerator, denominator) == expected