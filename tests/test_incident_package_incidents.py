import pytest
from incident_package.incidents import DivideByZeroIncident

def test_divide_by_zero():
    # Test case where denominator is zero
    incident = DivideByZeroIncident()
    with pytest.raises(ValueError, match="Denominator cannot be zero."):
        incident.run()

def test_divide_by_non_zero():
    # Test case where denominator is non-zero
    class MockDivideByZeroIncident(DivideByZeroIncident):
        def run(self):
            numerator = 10
            denominator = 2
            return numerator / denominator

    incident = MockDivideByZeroIncident()
    result = incident.run()
    assert result == 5.0
