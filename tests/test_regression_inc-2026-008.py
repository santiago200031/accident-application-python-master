from incident_package.controllers.remediation_controller import RemediationWorkflowIncident


def test_execute_remediation_pipeline_returns_zero_when_aggregated_missing_key():
    incident = RemediationWorkflowIncident()

    result = incident.execute_remediation_pipeline()

    assert result == 0


def test_run_returns_zero_instead_of_raising_keyerror_for_missing_aggregate_key():
    incident = RemediationWorkflowIncident()

    assert incident.run() == 0