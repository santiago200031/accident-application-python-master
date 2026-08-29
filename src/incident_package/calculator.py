from typing import Union

class Calculator:
    def calculate_rate(self, numerator: float, total_count: int) -> Union[float, None]:
        if total_count == 0:
            return 0.0
        return numerator / total_count