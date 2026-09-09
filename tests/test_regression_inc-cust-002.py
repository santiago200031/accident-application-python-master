import pytest

from incident_package.customer_exceptions.malformed_json_body import (
    MalformedJsonBodyIncident,
    delete_documents_http,
    query_requirements_http,
)


@pytest.mark.parametrize(
    "handler, body",
    [
        (
            query_requirements_http,
            '{"query": "x", "project_id": "x",',
        ),
        (
            query_requirements_http,
            "{'query': 'x'}",
        ),
        (
            query_requirements_http,
            '["not", "an", "object"]',
        ),
        (
            delete_documents_http,
            '{"partition_key": "customer-1",',
        ),
        (
            delete_documents_http,
            "{partition_key: 'customer-1'}",
        ),
        (
            delete_documents_http,
            '"not an object"',
        ),
    ],
)
def test_http_handlers_return_bad_request_for_malformed_or_non_object_json(
    handler, body
):
    response = handler(body)

    assert response == {
        "status": 400,
        "error": "Invalid JSON request body",
    }


def test_query_requirements_returns_bad_request_for_non_string_body():
    response = query_requirements_http(None)

    assert response == {
        "status": 400,
        "error": "Invalid JSON request body",
    }


def test_query_requirements_accepts_valid_json_object():
    response = query_requirements_http('{"query": "status:open"}')

    assert response == {
        "status": 200,
        "query": "status:open",
    }


def test_delete_documents_accepts_valid_json_object():
    response = delete_documents_http('{"partition_key": "customer-1"}')

    assert response == {
        "status": 200,
        "partition_key": "customer-1",
    }


def test_incident_reproduction_returns_controlled_bad_request():
    response = MalformedJsonBodyIncident().run()

    assert response == {
        "status": 400,
        "error": "Invalid JSON request body",
    }