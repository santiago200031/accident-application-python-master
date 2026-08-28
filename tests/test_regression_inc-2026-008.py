from incident_package.controllers.remediation_controller import RemediationWorkflowIncident


def test_execute_remediation_pipeline_returns_default_for_missing_key() -> None:
    incident = RemediationWorkflowIncident()
    assert incident.execute_remediation_pipeline() == 0


def test_run_returns_default_for_missing_key() -> None:
    incident = RemediationWorkflowIncident()
    assert incident.run() == 0