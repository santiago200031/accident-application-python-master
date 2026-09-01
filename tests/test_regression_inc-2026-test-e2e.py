import pytest

from incident_package.calculator import calculate_rate


def test_calculate_rate_returns_zero_for_empty_denominator():
    assert calculate_rate(5, 0) == 0.0


@pytest.mark.parametrize(
    ("numerator", "denominator", "expected"),
    [
        (0, 1, 0.0),
        (1, 2, 0.5),
        (3, 4, 0.75),
        (-2, 5, -0.4),
    ],
)
def test_calculate_rate_divides_nonzero_denominator(
    numerator, denominator, expected
):
    assert calculate_rate(numerator, denominator) == expected


def test_calculate_rate_returns_float_zero_for_empty_input_set():
    result = calculate_rate(0, 0)

    assert result == 0.0
    assert isinstance(result, float)