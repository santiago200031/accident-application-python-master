"""Calculation helpers for the incident package."""


def calculate_rate(numerator, denominator):
    """Return the rate represented by *numerator* over *denominator*.

    A zero denominator represents an undefined or unavailable rate.  Treat it
    as a safe zero rate rather than allowing a ZeroDivisionError to propagate.
    """
    if denominator == 0:
        return 0.0

    return numerator / denominator