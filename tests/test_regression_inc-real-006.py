from incident_package.controllers.alert_deduplicator_controller import (
    AlertRemediationCoordinator,
    DuplicateAlertRemediationIncident,
)


def test_duplicate_active_alert_dispatch_is_coalesced_without_runtime_error() -> None:
    coordinator = AlertRemediationCoordinator()

    result = coordinator.dispatch_remediation("alert-critical-exceptions-weu")

    assert result == {
        "dispatched": False,
        "alert_id": "alert-critical-exceptions-weu",
        "already_active": True,
    }
    assert "alert-critical-exceptions-weu" in coordinator.active_remediations


def test_incident_run_returns_controlled_duplicate_remediation_result() -> None:
    incident = DuplicateAlertRemediationIncident()

    assert incident.run() == {
        "dispatched": False,
        "alert_id": "alert-critical-exceptions-weu",
        "already_active": True,
    }


def test_first_dispatch_is_started_and_second_dispatch_is_coalesced() -> None:
    coordinator = AlertRemediationCoordinator()
    alert_id = "alert-new-service-euw"

    first_result = coordinator.dispatch_remediation(alert_id)
    second_result = coordinator.dispatch_remediation(alert_id)

    assert first_result == {"dispatched": True, "alert_id": alert_id}
    assert second_result == {
        "dispatched": False,
        "alert_id": alert_id,
        "already_active": True,
    }