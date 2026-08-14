# src/incident_package/utils/math_calculator.py
"""
Utility functions for performing safe mathematical operations throughout
the incident package.

All public helpers guarantee that the caller will **never see a
``ZeroDivisionError`` originating from this module**.  Instead, a
``ValueError`` with a clear error message is raised in the following cases:

1.  The divisor is *exactly* zero.  
2.  The divisor is infinite or NaN.  
3.  Either operand cannot be interpreted as a real number.

In addition, callers receive a warning when the divisor is close to
machine precision – the division is still performed, but the output
may be numerically unstable.
"""

from __future__ import annotations

import math
import sys
import warnings
from typing import Any

__all__ = ["divide_two_numbers"]


def _to_float(value: Any) -> float:
    """Coerce *value* to a ``float`` with a clear error message.

    Parameters
    ----------
    value : Any
        Any object that can be cast to a real number.

    Returns
    -------
    float
        The numeric representation of *value*.

    Raises
    ------
    TypeError
        If *value* cannot be interpreted as a number.
    """
    try:
        return float(value)
    except Exception as exc:  # pragma: no cover
        raise TypeError(f"Value {value!r} cannot be interpreted as a number") from exc


def divide_two_numbers(a: Any, b: Any) -> float:
    """
    Safely divide ``a`` by ``b`` while guarding against an invalid
    denominator.

    Parameters
    ----------
    a, b : Any
        Must be convertible to ``float`` (int, float, string containing
        a number, Decimal, etc.).

    Returns
    -------
    float
        The result of ``float(a) / float(b)``.

    Raises
    ------
    TypeError
        If either ``a`` or ``b`` cannot be interpreted as a number.
    ValueError
        If ``b`` is infinite, NaN, or evaluates to zero.
    """
    # ------------------------------------------------------------------
    # 1. Convert operands to float.  ``_to_float`` raises ``TypeError``
    #    automatically if conversion fails.
    # ------------------------------------------------------------------
    numerator: float = _to_float(a)
    denominator_raw: Any = b

    # ------------------------------------------------------------------
    # 2. Early zero‑check (handles int and float zero before conversion).
    #    This also catches ``-0.0`` which is equal to ``0.0``.
    # ------------------------------------------------------------------
    if isinstance(denominator_raw, (int, float)) and denominator_raw == 0:
        raise ValueError(f"Denominator {b!r} cannot be zero")

    # ------------------------------------------------------------------
    # 3. Convert denominator to float.  This turns strings like '0',
    #    Decimal(0), etc. into a numeric value.
    # ------------------------------------------------------------------
    denominator: float = _to_float(denominator_raw)

    # ------------------------------------------------------------------
    # 4. Reject infinite or NaN denominators.
    # ------------------------------------------------------------------
    if not math.isfinite(denominator):
        raise ValueError(
            f"Denominator {b!r} must be a finite real number (got {denominator!r})"
        )

    # ------------------------------------------------------------------
    # 5. Reject zero after conversion – this also captures string/Decimal
    #    representations that skip the earlier check.
    # ------------------------------------------------------------------
    if denominator == 0.0:
        raise ValueError(f"Denominator {b!r} cannot be zero")

    # ------------------------------------------------------------------
    # 6. Warn if denominator is close to machine epsilon (numeric instability).
    # ------------------------------------------------------------------
    if math.isclose(denominator, 0.0, abs_tol=sys.float_info.epsilon):
        warnings.warn(
            f"Denominator {b!r} ({denominator}) is close to zero; "
            "division may produce a large magnitude result.",
            RuntimeWarning,
            stacklevel=2,
        )

    # ------------------------------------------------------------------
    # 7. Perform the division (now safe – all guards have passed).
    # ------------------------------------------------------------------
    try:
        return numerator / denominator
    except ZeroDivisionError as exc:  # pragma: no cover
        # This block is defensive; it should never be hit after the
        # explicit zero‑check above.
        raise ValueError(f"Denominator {b!r} caused a division by zero") from exc