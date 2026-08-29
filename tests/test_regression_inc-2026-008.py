from incident_package.controllers.remediation_controller import RemediationWorkflowIncident


def test_aggregation_reproduces_missing_key_scenario():
    metric_rows = RemediationWorkflowIncident._filter_valid_metrics(
        RemediationWorkflowIncident._load_initial_metrics()
    )

    aggregated_stats = RemediationWorkflowIncident._aggregate_stats(metric_rows)

    assert aggregated_stats == {"total": 60}
    assert "missing_key" not in aggregated_stats


def test_remediation_pipeline_returns_default_for_missing_statistic():
    incident = RemediationWorkflowIncident()

    assert incident.execute_remediation_pipeline() == 0
    assert incident.run() == 0