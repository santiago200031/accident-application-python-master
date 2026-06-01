import pytest
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter

@pytest.fixture
def setup_adapter():
    """Fixture to provide a fresh instance of BrokenMCPAdapter."""
    return BrokenMCPAdapter()

def test_calculate_risk_zero_checks_division_by_zero(setup_adapter):
    """Tests calculate_risk when checks is zero, expecting 0 risk score."""
    # Setup scenario where checks is 0
    setup_adapter.checks = 0
    setup_adapter.incidents = 5  # Non-zero incidents

    # Act
    risk_score = setup_adapter.calculate_risk()

    # Assert: Should return 0 instead of raising ZeroDivisionError
    assert risk_score == 0

def test_calculate_risk_normal_operation(setup_adapter):
    """Tests calculate_risk with normal, non-zero checks and incidents."""
    # Setup scenario where checks is non-zero
    setup_adapter.checks = 4
    setup_adapter.incidents = 8

    # Act
    risk_score = setup_adapter.calculate_risk()

    # Assert: Should perform normal division (8 / 4 = 2.0)
    assert risk_score == 2.0

def test_calculate_risk_zero_incidents_non_zero_checks(setup_adapter):
    """Tests calculate_risk when incidents is zero, but checks is non-zero."""
    # Setup scenario where incidents is 0
    setup_adapter.checks = 5
    setup_adapter.incidents = 0

    # Act
    risk_score = setup_adapter.calculate_risk()

    # Assert: Should perform normal division (0 / 5 = 0.0)
    assert risk_score == 0.0
