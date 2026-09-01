"""Application entry point and safe arithmetic helpers."""


class MathCalculator:
    """Perform arithmetic operations used by the application."""

    @staticmethod
    def divide_two_numbers(numerator, denominator):
        """Return ``numerator / denominator`` or ``0.0`` for a zero denominator.

        A zero denominator represents an empty or otherwise invalid count in
        the aggregation path. Returning a neutral numeric value keeps the
        application running without raising ``ZeroDivisionError``.
        """
        if denominator == 0:
            return 0.0
        return numerator / denominator

    def run(self, total_amount=0.0, total_count=0):
        """Calculate the average amount for the supplied totals."""
        return self.divide_two_numbers(total_amount, total_count)


def divide_two_numbers(numerator, denominator):
    """Safely divide two numbers, returning ``0.0`` for zero denominators."""
    return MathCalculator.divide_two_numbers(numerator, denominator)


if __name__ == "__main__":
    # Keep direct execution harmless when no records are available.
    print(MathCalculator().run())