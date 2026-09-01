import pytest

from main import MathCalculator, divide_two_numbers


def test_divide_two_numbers_returns_zero_for_zero_denominator():
    assert MathCalculator.divide_two_numbers(125.0, 0) == 0.0


def test_run_with_empty_totals_returns_neutral_average():
    assert MathCalculator().run() == 0.0


def test_module_level_division_helper_handles_zero_denominator():
    assert divide_two_numbers(42, 0) == 0.0


@pytest.mark.parametrize(
    ("numerator", "denominator", "expected"),
    [
        (10, 2, 5.0),
        (-9, 3, -3.0),
        (0, 7, 0.0),
    ],
)
def test_nonzero_division_is_unchanged(numerator, denominator, expected):
    assert MathCalculator.divide_two_numbers(numerator, denominator) == expected