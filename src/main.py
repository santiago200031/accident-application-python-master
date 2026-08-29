# src/main.py
def divide_two_numbers(numerator, denominator):
    if denominator == 0:
        return 0.0
    return numerator / denominator

class Calculator:
    def __init__(self, total_count):
        self.total_count = total_count

    def run(self):
        result = divide_two_numbers(10, self.total_count)
        print(f"Result: {result}")

if __name__ == "__main__":
    calculator = Calculator(total_count=0)  # Example case where total_count might be zero
    calculator.run()