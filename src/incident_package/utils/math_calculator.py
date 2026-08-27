from __future__ import annotations

from incident_package.base import Incident


class DivideByZeroIncident(Incident):
    mode = "divide-by-zero"

    def divide_two_numbers(self, numerator: float, denominator: float) -> None | float:
        if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise TypeError("Both inputs must be numbers")
        
        if denominator == 0:
            raise ZeroDivisionError(f"Cannot divide {numerator} by zero. Input values may indicate empty/invalid data.")
        
        return numerator / denominator

    def run(self) -> None | float:
        total_amount = 5.0
        total_count = 0.0
        
        if not isinstance(total_amount, (int, float)):
            raise TypeError("total_amount must be a number")
            
        if not isinstance(total_count, (int, float)):
            raise TypeError("total_count must be a number")
        
        return self.divide_two_numbers(total_amount, total_count)