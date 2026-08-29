# src/incident_package/calculator.py

def calculate_rate(numerator, denominator):
    if denominator == 0:
        return 0.0
    else:
        return numerator / denominator