# src/main.py

def divide_two_numbers(numerator, denominator):
    # Guard against division by zero by returning 0.0 if denominator is 0
    if denominator == 0:
        return 0.0
    return numerator / denominator

# Example usage that might trigger the error
if __name__ == '__main__':
    result = divide_two_numbers(10, 0)
    print(f'Result of division: {result}')