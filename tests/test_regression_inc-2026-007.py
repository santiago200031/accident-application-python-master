import pytest

from incident_package.services.command_executor_service import BranchChaosIncident


def test_run_handles_nonzero_command_without_raising_called_process_error():
    incident = object.__new__(BranchChaosIncident)

    try:
        output = incident.run()
    except subprocess.CalledProcessError as exc:
        pytest.fail(f"non-zero command unexpectedly raised: {exc}")

    assert output == ""