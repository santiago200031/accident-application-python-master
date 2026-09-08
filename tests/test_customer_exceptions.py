"""Tests for anonymized customer-exception scenarios (C1 to C6).

Each test describes the *fixed* contract; the intentionally broken
implementation under src/incident_package/customer_exceptions/ fails these
until repaired (tests-first target for the benchmark agent).
"""

from __future__ import annotations

import pytest

from incident_package.customer_exceptions.broken_alert_scoping import (
    MonitoringBackend,
    should_fire,
)
from incident_package.customer_exceptions.malformed_json_body import (
    delete_documents_http,
    query_requirements_http,
)
from incident_package.customer_exceptions.none_dereference_missing_doc import (
    DocumentStore,
    process_document,
)
from incident_package.customer_exceptions.nosql_injection import (
    similarity_search_by_filenames,
)
from incident_package.customer_exceptions.path_traversal_idor import FileStore
from incident_package.customer_exceptions.unauthenticated_api import BackendRoutes


def test_c1_unauthenticated_api_requires_token():
    """C1 (V1): unauthorized request must not return thread data."""
    routes = BackendRoutes(auth_enabled=True)
    identity = routes.extract_caller_identity(None)
    assert identity is None
    # When auth is enabled, list_threads must reject a caller without a token.
    with pytest.raises(Exception):
        routes.list_threads(None)


def test_c2_malformed_json_returns_400_not_500():
    """C2 (V2): malformed JSON must not raise an unhandled JSONDecodeError."""
    bad_body = '{"query": "x", "project_id": "x",'
    res = query_requirements_http(bad_body)
    assert res.get("status") == 400
    invalid = '{"partition_key": "x",'
    assert delete_documents_http(invalid).get("status") == 400


def test_c3_path_traversal_blocked_and_owned_only():
    """C3 (V3): traversal is rejected and cross-tenant reads are forbidden."""
    store = FileStore()
    with pytest.raises(Exception):
        store.get_content("thread_a1f1c1c8", "../../../../etc/passwd")
    with pytest.raises(Exception):
        store.get_content("thread_cece7b9f", "output/requirements_extracted.json")


def test_c4_nosql_injection_parameterized():
    """C4 (V4): malicious filename must not break the query or bypass filters."""
    results = similarity_search_by_filenames('x" OR 1=1 -- ')
    assert isinstance(results, list)
    assert results == []


def test_c5_missing_document_returns_404_not_none_deref():
    """C5 (V5): missing document must return 404 rather than AttributeError."""
    store = DocumentStore()
    # Fixed behavior: no exception; a 404-style result is returned instead.
    result = process_document("doc-nonexistent", store)
    assert result is None


def test_c6_alert_scoping_evaluates_telemetry():
    """C6 (V6): App Insights-scoped rules must reflect actual telemetry."""
    backend = MonitoringBackend()
    backend.push({"level": "ERROR", "message": "Exception in ASGI application"})
    # After the fix, telemetry reaches App Insights so its rule fires too.
    assert should_fire("app-insights", backend) is True
    assert should_fire("log-analytics", backend) is True
