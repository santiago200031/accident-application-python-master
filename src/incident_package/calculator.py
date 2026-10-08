"""Calculation helpers for incident processing."""


def calculate_rate(numerator, denominator):
    """Calculate a rate while safely handling an empty denominator.

    A zero denominator represents an empty or unavailable input set. In that
    case, return a neutral rate of ``0.0`` rather than raising
    ``ZeroDivisionError``.
    """
    if denominator == 0:
        return 0.0

    return numerator / denominator