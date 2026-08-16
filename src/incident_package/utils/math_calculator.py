from __future__ import annotations

import logging
from incident_package.base import Incident

# Configure a logger for this module
logger = logging.getLogger(__name__)


class DivideByZeroIncident(Incident):
    """Incident that demonstrates safe division handling."""

    mode = "divide-by-zero"

    def divide_two_numbers(self, numerator: float, denominator: float) -> float:
        """
        Safely divide two numbers.

        Parameters
        ----------
        numerator : float
            The dividend.
        denominator : float
            The divisor. Must not be zero.

        Returns
        -------
        float
            The result of the division.

        Raises
        ------
        ValueError
            If the denominator is zero.
        """
        if denominator == 0:
            # Log a warning with the context for easier debugging.
            logger.warning(
                "Attempted to divide %s by zero. Numerical context: numerator=%s",
                numerator,
                numerator,
            )
            raise ValueError("Denominator cannot be zero")

        return numerator / denominator

    def run(self) -> float:
        """
        Execute the incident. The original implementation used a fixed
        denominator of `0.0`, which caused a ZeroDivisionError.  
        This method now relies on the validated `divide_two_numbers` method.
        """
        total_amount = 5.0
        total_count = 0.0
        return self.divide_two_numbers(total_amount, total_count)