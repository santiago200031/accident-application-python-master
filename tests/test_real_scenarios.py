"""Tests for anonymized real-world incident scenarios (R1 to R8) from sysengcopilotv3."""

from __future__ import annotations

import pytest

from incident_package.services.streaming_pipeline_service import execute_stream_pipeline
from incident_package.repositories.blob_storage_repository import MockBlobContainerClient
from incident_package.controllers.queue_consumer_controller import process_queue_message
from incident_package.utils.cloud_config_loader import load_cloud_service_config
from incident_package.services.infra_metadata_service import resolve_infrastructure_host
from incident_package.controllers.alert_deduplicator_controller import AlertRemediationCoordinator
from incident_package.services.api_boundary_service import service_error_boundary
from incident_package.utils.telemetry_metric_calculator import compute_incident_resolution_rate


def test_r1_streaming_pipeline_does_not_reraise():
    """R1 (PR #94): Handled errors yield error chunk without crashing stream."""
    items = ["item1", "trigger_error", "item2"]
    results = list(execute_stream_pipeline(items))
    assert len(results) == 3
    assert results[0]["status"] == "ok"
    assert results[1]["status"] == "error"
    assert results[2]["status"] == "ok"


def test_r2_storage_container_conflict():
    """R2 (PR #110): Pre-existing storage containers do not crash pipeline."""
    client = MockBlobContainerClient(existing_containers={"telemetry-archive"})
    # Should not raise FileExistsError if idempotently guarded
    res = client.create_container("telemetry-archive")
    assert res is not None


def test_r3_malformed_queue_payload():
    """R3 (PR #79/#81): Malformed queue messages return fallback error rather than crashing."""
    res = process_queue_message("CORRUPTED_QUEUE_PAYLOAD_NON_JSON")
    assert res is not None
    assert res.get("status") in ("error", "invalid", "fallback")


def test_r4_cloud_config_loader_defaults():
    """R4 (PR #76/#90): Missing cloud env vars fall back safely."""
    cfg = load_cloud_service_config()
    assert isinstance(cfg, dict)
    assert "endpoint" in cfg


def test_r5_infra_metadata_null_safe():
    """R5 (PR #82): Null outputs return safe fallback or empty string."""
    host = resolve_infrastructure_host(None)
    assert host in ("", "unknown", "localhost")


def test_r6_alert_deduplication():
    """R6 (PR #71/#106): Duplicate remediation does not crash coordinator."""
    coordinator = AlertRemediationCoordinator()
    res = coordinator.dispatch_remediation("alert-critical-exceptions-weu")
    assert res is not None


def test_r7_service_error_boundary():
    """R7 (PR #84/#85): Boundary intercepts unhandled exceptions returning JSON."""
    res = service_error_boundary({"authorized": False})
    assert isinstance(res, dict)
    assert res.get("status") in (403, 500, "error")


def test_r8_metric_zero_division():
    """R8 (PR #67): Zero alerts returns 0.0 without ZeroDivisionError."""
    rate = compute_incident_resolution_rate(0, 0)
    assert rate == 0.0
