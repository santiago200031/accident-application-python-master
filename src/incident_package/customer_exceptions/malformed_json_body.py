from __future__ import annotations

import json
from typing import Any

from incident_package.base import Incident


_BAD_REQUEST_RESPONSE: dict[str, Any] = {
    "status": 400,
    "error": "Invalid JSON request body",
}


def _parse_json_object(body: str) -> dict[str, Any] | None:
    """Parse a request body, returning None when it is not a JSON object."""
    try:
        data = json.loads(body)
    except (json.JSONDecodeError, TypeError):
        return None

    return data if isinstance(data, dict) else None


def query_requirements_http(body: str) -> dict[str, Any]:
    """Route handler that safely parses the request JSON."""
    data = _parse_json_object(body)
    if data is None:
        return _BAD_REQUEST_RESPONSE.copy()

    return {"status": 200, "query": data.get("query")}


def delete_documents_http(body: str) -> dict[str, Any]:
    """Route handler that safely parses the request JSON."""
    data = _parse_json_object(body)
    if data is None:
        return _BAD_REQUEST_RESPONSE.copy()

    return {"status": 200, "partition_key": data.get("partition_key")}


class MalformedJsonBodyIncident(Incident):
    mode = "cust-c2-malformed-json"

    def run(self) -> dict[str, Any]:
        # Truncated JSON body, exactly as reproduced against the live backend.
        bad_body = '{"query": "x", "project_id": "x",'
        return query_requirements_http(bad_body)