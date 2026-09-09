from incident_package.controllers.alert_deduplicator_controller import DuplicateAlertRemediationIncident

def test_duplicate_remediation_dispatch():
    incident = DuplicateAlertRemediationIncident()
    result = incident.run()
    
    # Assert the fixed behavior: return a safe default instead of raising an exception
    assert result == {
        "dispatched": False,
        "alert_id": "alert-critical-exceptions-weu",
        "error": "already active"
    }

def test_new_remediation_dispatch():
    incident = DuplicateAlertRemediationIncident()
    # Dispatch a new alert that is not already active
    result = incident.coordinator.dispatch_remediation("new-alert-id")
    
    # Assert the successful dispatch of a new alert
    assert result == {
        "dispatched": True,
        "alert_id": "new-alert-id"
    }