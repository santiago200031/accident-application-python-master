from incident_package.controllers.remediation_controller import RemediationWorkflowIncident


def test_execute_remediation_pipeline_returns_zero_when_missing_stat_is_absent():
    incident = RemediationWorkflowIncident()

    assert incident.execute_remediation_pipeline() == 0


def test_run_returns_zero_when_aggregated_stats_do_not_contain_missing_key():
    incident = RemediationWorkflowIncident()

    assert incident.run() == 0