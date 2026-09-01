"""Application entry point and safe count-based calculation helpers."""


def divide_two_numbers(numerator, denominator):
    """Divide *numerator* by *denominator* safely.

    An empty input set can produce a denominator of zero.  In that case,
    return a neutral numeric result rather than allowing ZeroDivisionError to
    escape to the application boundary.
    """
    if denominator == 0:
        return 0.0
    return numerator / denominator


def run(total_amount=0, total_count=0):
    """Calculate the average amount per item.

    ``total_count`` may be zero when there are no input records or when all
    records have been filtered out.  ``divide_two_numbers`` handles that case
    by returning ``0.0``.
    """
    return divide_two_numbers(total_amount, total_count)


if __name__ == "__main__":
    print(run())