# File src/main.py

def run(total_count, total_errors):
    if total_count == 0:
        return 0.0
    error_rate = total_errors / total_count
    return error_rate