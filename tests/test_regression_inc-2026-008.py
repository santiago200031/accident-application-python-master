from incident_package.controllers.remediation_controller import RemediationWorkflowIncident


def test_execute_remediation_pipeline_returns_zero_when_missing_key_is_absent():
    incident = RemediationWorkflowIncident()

    result = incident.execute_remediation_pipeline()

    assert result == 0


def test_run_returns_zero_when_aggregated_stats_lack_missing_key():
    incident = RemediationWorkflowIncident()

    assert incident.run() == 0