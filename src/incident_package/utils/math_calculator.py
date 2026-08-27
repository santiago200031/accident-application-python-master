from __future__ import annotations

from incident_package.base import Incident


class DivideByZeroIncident(Incident):
    mode = "divide-by-zero"

    def divide_two_numbers(self, numerator: float, denominator: float) -> float:
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        return numerator / denominator

    def run(self) -> float:
        total_amount = 5.0
        total_count = 0.0
        return self.divide_two_numbers(total_amount, total_count)