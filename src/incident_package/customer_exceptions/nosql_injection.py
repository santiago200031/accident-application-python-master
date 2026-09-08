from __future__ import annotations

from typing import Any
from incident_package.base import Incident


class CosmosClient:
    """Minimal stand-in for the Cosmos SQL client."""

    def query_with_in_clause(self, filenames: object) -> list[dict[str, Any]]:
        # BUG (Anonymized C4): raw string interpolation into the IN (...) clause.
        placeholders = ", ".join(f'"{f}"' for f in filenames)
        in_clause = f"c.document_filename IN ({placeholders})"
        # A malformed IN clause surfaces as a 400 BadRequest from the backend.
        if any(marker in in_clause for marker in ("--", "OR 1=1", '""')):
            raise ValueError(f"BadRequest: malformed query: {in_clause}")
        return []


def similarity_search_by_filenames(filename: str) -> list[dict[str, Any]]:
    client = CosmosClient()
    # BUG (Anonymized C4): passes a string instead of a list -> iterates chars
    return client.query_with_in_clause(filename)


class NosqlInjectionIncident(Incident):
    mode = "cust-c4-nosql-injection"

    def run(self) -> list[dict[str, Any]]:
        malicious_filename = 'x" OR 1=1 -- '
        return similarity_search_by_filenames(malicious_filename)
