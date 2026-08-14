# src/incident_package/calculator.py
"""
Utility module for calculating rates of incident events.

Public API
----------
calculate_rate(events, timeframe) -> Optional[float]
    Compute events per unit time.

The implementation validates its inputs and protects against a
``ZeroDivisionError`` by ensuring that the divisor is a finite,
strictly‑positive number before performing the division.  If the
division cannot be performed safely the function logs a warning and
returns ``None``.
"""

from __future__ import annotations

import logging
import math
from typing import Any, Final, Optional

__all__: Final = ["calculate_rate"]

# --------------------------------------------------------------------------- #
# Logging
# --------------------------------------------------------------------------- #
_logger = logging.getLogger(__name__)

# --------------------------------------------------------------------------- #
# Internal helpers
# --------------------------------------------------------------------------- #
def _validate_numeric(value: Any, name: str) -> float:
    """
    Convert ``value`` to a float and validate it.

    Parameters
    ----------
    value
        The value to convert.
    name
        Name used in error messages.

    Returns
    -------
    float
        The numeric value.

    Raises
    ------
    ValueError
        If ``value`` cannot be interpreted as a real number.
    """
    if value is None:
        raise ValueError(f"{name} cannot be None")

    # ``complex`` is accepted only if the imaginary part is zero.
    if isinstance(value, complex):
        if value.imag != 0:
            raise ValueError(
                f"{name} cannot contain a non‑zero imaginary part: {value!r}"
            )
        return float(value.real)

    # The common numeric types can be trusted to represent a real number.
    if isinstance(value, (int, float)):
        return float(value)

    # Try converting strings or other objects that implement __float__.
    try:
        return float(value)
    except (TypeError, ValueError) as exc:  # pragma: no cover
        raise ValueError(
            f"{name} must be a numeric value (got {value!r}, "
            f"type={type(value).__name__})"
        ) from exc


# --------------------------------------------------------------------------- #
# Public API
# --------------------------------------------------------------------------- #
def calculate_rate(events: Any, timeframe: Any) -> Optional[float]:
    """
    Calculate incidents per unit time.

    Parameters
    ----------
    events
        Number of events that occurred during the time period.
        Must be convertible to a real ``float``.
    timeframe
        Length of the time period (seconds, minutes, …).
        Must be a positive, finite number.
        A non‑positive, infinite, or NaN value results in ``None``
        instead of raising a ``ZeroDivisionError``.

    Returns
    -------
    Optional[float]
        ``float`` number of events per unit time, or ``None`` when the
        division cannot be performed safely.

    Raises
    ------
    ValueError
        If either argument cannot be interpreted as a number,
        or if ``events`` is a complex number with a non‑zero imaginary part.
    """
    # 1️⃣ Convert & validate the inputs
    events_num: float = _validate_numeric(events, "events")
    timeframe_num: float = _validate_numeric(timeframe, "timeframe")

    # 2️⃣ Guard: non‑finite or non‑positive timeframe – no division possible.
    if not math.isfinite(timeframe_num):
        _logger.warning(
            "%s received a non‑finite timeframe (%s); returning None.",
            calculate_rate.__name__,
            timeframe_num,
        )
        return None

    if timeframe_num <= 0.0:
        # Log the specific problem (zero or negative) to aid telemetry.
        issue = "zero" if timeframe_num == 0.0 else "negative"
        _logger.warning(
            "%s received an invalid timeframe (%s %): %s; returning None.",
            calculate_rate.__name__,
            issue,
            timeframe_num,
        )
        return None

    # 3️⃣ Optional guard: non‑finite numerator – unlikely but safe.
    if not math.isfinite(events_num):
        _logger.warning(
            "%s received a non‑finite events value (%s); returning None.",
            calculate_rate.__name__,
            events_num,
        )
        return None

    # 4️⃣ Safely divide – guard guarantees we never hit ZeroDivisionError.
    result: float = events_num / timeframe_num

    # 5️⃣ Post‑division sanity check (guard unnecessary but defensive).
    if not math.isfinite(result):
        _logger.warning(
            "%s produced a non‑finite result (%s); returning None.",
            calculate_rate.__name__,
            result,
        )
        return None

    # 6️⃣ Success path
    _logger.debug(
        "%s: events=%s, timeframe=%s -> %s",
        calculate_rate.__name__,
        events_num,
        timeframe_num,
        result,
    )
    return result