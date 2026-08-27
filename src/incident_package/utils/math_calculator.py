from __future__ import annotations

import logging

from incident_package.base import Incident


class DivideByZeroIncident(Incident):
    mode = "divide-by-zero"

    def divide_two_numbers(self, numerator: float, denominator: float) -> float:
        if denominator == 0.0 or denominator is None:
            raise ValueError(f"Division by zero not allowed. Denominator must be > 0 (got {denominator}).")
        return numerator / denominator

    def run(self) -> float:
        total_amount = 5.0
        
        if len(total_count := self.get_total_count()) == 0 or total_count is None:
            raise ValueError("Cannot divide by zero count.")
        
        return self.divide_two_numbers(total_amount, total_count)