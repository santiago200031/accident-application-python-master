from __future__ import annotations

import json
from typing import Any
from incident_package.base import Incident


def query_requirements_http(body: str) -> dict[str, Any]:
    """Route handler that parses the request JSON with no guard."""
    # BUG (Anonymized C2): await req.json() without try/except -> JSONDecodeError
    data = json.loads(body)
    return {"status": 200, "query": data.get("query")}


def delete_documents_http(body: str) -> dict[str, Any]:
    # BUG (Anonymized C2): same unguarded parse on a second endpoint
    data = json.loads(body)
    return {"status": 200, "partition_key": data.get("partition_key")}


class MalformedJsonBodyIncident(Incident):
    mode = "cust-c2-malformed-json"

    def run(self) -> dict[str, Any]:
        # Truncated JSON body, exactly as reproduced against the live backend.
        bad_body = '{"query": "x", "project_id": "x",'
        return query_requirements_http(bad_body)
