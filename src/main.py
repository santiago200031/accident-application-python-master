# src/main.py

def divide_two_numbers(numerator, denominator):
    if denominator == 0:
        return 0.0
    return numerator / denominator


class AccidentCalculator:
    def __init__(self, accidents):
        self.accidents = accidents

    def calculate_average(self):
        total_count = len(self.accidents)
        if total_count == 0:
            return 0.0
        return divide_two_numbers(sum(accident['severity'] for accident in self.accidents), total_count)


def run():
    accidents = [
        {'id': 1, 'severity': 3},
        {'id': 2, 'severity': 2},
        {'id': 3, 'severity': 0}
    ]
    calculator = AccidentCalculator(accidents)
    average_severity = calculator.calculate_average()
    print(f"Average Severity: {average_severity}")

if __name__ == '__main__':
    run()