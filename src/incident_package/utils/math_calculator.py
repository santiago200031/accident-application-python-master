# src/incident_package/utils/math_calculator.py
"""
Utility module for performing basic mathematical operations
within the Incident framework.

The module provides a small helper that safely divides two
floating‑point numbers.  If the divisor is zero or an invalid
value is supplied, a :class:`ValueError` is raised instead of
letting a :class:`ZeroDivisionError` propagate.  This keeps
client code from crashing and gives callers a clear, predictable
exception type to handle.

The rest of the module (including the :class:`DivideByZeroIncident`
class that intentionally triggers the guard) remains unchanged
from the original implementation, ensuring that existing
workflows continue to operate as before.

The module follows PEP‑8 style guidelines and contains
comprehensive docstrings for every public API.
"""

from __future__ import annotations

from numbers import Number as _Num
from typing import Union

from incident_package.base import Incident

# A simple type alias used throughout the module.
Number = Union[int, float]


class DivideByZeroIncident(Incident):
    """
    An Incident that demonstrates a division operation.

    The ``mode`` attribute is used by the Incident framework to
    identify the type of incident.  The :py:meth:`run` method
    performs a division that will intentionally trigger a
    division‑by‑zero scenario when ``total_count`` is zero.
    """

    mode = "divide-by-zero"

    @staticmethod
    def divide_two_numbers(numerator: Number, denominator: Number) -> float:
        """
        Divide two numbers with zero‑division protection.

        Parameters
        ----------
        numerator : Number
            The dividend.  Must be numeric.
        denominator : Number
            The divisor.  Must be numeric and non‑zero.

        Returns
        -------
        float
            The result of the division.

        Raises
        ------
        ValueError
            If ``denominator`` is zero or not a numeric value,
            or if ``numerator`` is not numeric.
        TypeError
            If either argument cannot be converted to a float.
        """
        # Validate the numerator first.
        if not isinstance(numerator, _Num):
            raise ValueError(f"Numerator must be numeric, got {type(numerator).__name__}")

        # Guard against an invalid denominator.
        if not isinstance(denominator, _Num):
            raise ValueError(f"Denominator must be numeric, got {type(denominator).__name__}")

        # Convert to float for comparison and arithmetic.
        denom_flt = float(denominator)
        if denom_flt == 0.0:
            raise ValueError("Divisor cannot be zero")

        return float(numerator) / denom_flt

    def run(self) -> float:
        """
        Execute the incident logic.

        Intentionally uses a zero divisor to trigger the
        guard in :meth:`divide_two_numbers`.  In a real‑world
        scenario, downstream code would catch the raised
        :class:`ValueError` and handle it appropriately.
        """
        total_amount = 5.0
        total_count = 0.0
        return self.divide_two_numbers(total_amount, total_count)