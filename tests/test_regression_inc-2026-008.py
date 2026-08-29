from incident_package.controllers.remediation_controller import RemediationWorkflowIncident


def test_execute_remediation_pipeline_defaults_missing_statistic_to_zero():
    workflow = RemediationWorkflowIncident()

    initial_metrics = workflow._load_initial_metrics()
    filtered_metrics = workflow._filter_valid_metrics(initial_metrics)
    aggregated_stats = workflow._aggregate_stats(filtered_metrics)

    assert "missing_key" not in aggregated_stats
    assert workflow.execute_remediation_pipeline() == 0


def test_run_returns_zero_when_missing_statistic_is_not_aggregated():
    workflow = RemediationWorkflowIncident()

    assert workflow.run() == 0