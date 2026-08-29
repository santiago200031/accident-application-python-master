# src/main.py

def divide_two_numbers(numerator, denominator):
    if denominator == 0:
        return 0.0
    return numerator / denominator

class Application:
    def __init__(self, data):
        self.data = data

    def run(self):
        total_count = len(self.data)
        if total_count == 0:
            average_value = 0.0
        else:
            sum_values = sum(self.data)
            average_value = divide_two_numbers(sum_values, total_count)
        return average_value