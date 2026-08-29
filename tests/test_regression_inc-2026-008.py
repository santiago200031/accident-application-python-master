from incident_package.controllers.remediation_controller import RemediationWorkflowIncident


def test_execute_remediation_pipeline_returns_aggregated_total():
    incident = RemediationWorkflowIncident()

    assert incident.execute_remediation_pipeline() == 60


def test_execute_remediation_pipeline_returns_zero_when_total_is_absent(monkeypatch):
    incident = RemediationWorkflowIncident()
    monkeypatch.setattr(
        incident,
        "_aggregate_stats",
        lambda metric_rows: {},
    )

    assert incident.execute_remediation_pipeline() == 0