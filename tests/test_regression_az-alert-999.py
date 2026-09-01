from main import divide_two_numbers, run


def test_divide_two_numbers_returns_zero_for_zero_denominator():
    assert divide_two_numbers(125, 0) == 0.0


def test_run_handles_empty_input_totals():
    assert run() == 0.0
    assert run(total_amount=125, total_count=0) == 0.0


def test_divide_two_numbers_still_divides_nonzero_denominators():
    assert divide_two_numbers(10, 4) == 2.5


def test_run_calculates_average_for_nonempty_input():
    assert run(total_amount=30, total_count=6) == 5.0