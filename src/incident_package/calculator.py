"""Rate calculation utilities.

The rate calculation must handle empty input sets gracefully.  An empty set
produces a denominator of zero, for which a rate of ``0.0`` is returned.
"""


def calculate_rate(numerator, denominator):
    """Calculate a rate without raising for an empty denominator.

    Args:
        numerator: The number of successful or qualifying events.
        denominator: The total number of events.

    Returns:
        The calculated rate, or ``0.0`` when ``denominator`` is zero.
    """
    if denominator == 0:
        return 0.0

    return numerator / denominator


__all__ = ["calculate_rate"]