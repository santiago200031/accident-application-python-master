from typing import Union

def calculate_rate(numerator: int, denominator: int) -> float:
    """
    Calculate the rate by dividing numerator by denominator.
    Handles division by zero by returning 0.0.
    """
    if denominator == 0:
        return 0.0
    return numerator / denominator

class Calculator:
    def __init__(self, data):
        self.data = data

    def compute(self):
        total_count = sum(self.data)
        rate = calculate_rate(100, total_count)
        return rate