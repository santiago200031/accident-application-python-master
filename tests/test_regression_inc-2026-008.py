from incident_package.controllers.remediation_controller import RemediationWorkflowIncident


def test_remediation_pipeline_handles_missing_configuration_without_keyerror(monkeypatch):
    monkeypatch.delenv("AZURE_SERVICE_ENDPOINT", raising=False)

    incident = RemediationWorkflowIncident()

    assert incident.execute_remediation_pipeline() == 0
    assert incident.run() == 0