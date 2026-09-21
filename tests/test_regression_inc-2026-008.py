import pytest

from incident_package.controllers.remediation_controller import (
    RemediationWorkflowIncident,
)


def test_remediation_pipeline_returns_default_when_cloud_endpoint_is_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("AZURE_SERVICE_ENDPOINT", raising=False)

    workflow = object.__new__(RemediationWorkflowIncident)

    assert workflow.execute_remediation_pipeline() == 0