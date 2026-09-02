from incident_package.controllers.remediation_controller import RemediationWorkflowIncident


def test_execute_remediation_pipeline_defaults_missing_aggregate_key_to_zero():
    workflow = RemediationWorkflowIncident()

    result = workflow.execute_remediation_pipeline()

    assert result == 0


def test_run_returns_pipeline_result_when_aggregate_has_no_missing_key():
    workflow = RemediationWorkflowIncident()

    assert workflow.run() == 0