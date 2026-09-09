from __future__ import annotations

from typing import Any

from incident_package.base import Incident


class CosmosClient:
    """Minimal stand-in for the Cosmos SQL client."""

    def query_with_in_clause(self, filenames: object) -> list[dict[str, Any]]:
        """Query filenames without placing user-provided values in SQL text."""
        if isinstance(filenames, str):
            values = [filenames]
        elif isinstance(filenames, (list, tuple)):
            values = list(filenames)
        else:
            return []

        # Invalid input is not sent to Cosmos. Quotes and other SQL-looking
        # characters remain valid filename data because they are parameters.
        if not values or not all(
            isinstance(filename, str) and filename.strip() for filename in values
        ):
            return []

        query = (
            "SELECT * FROM c "
            "WHERE ARRAY_CONTAINS(@filenames, c.document_filename)"
        )
        parameters = [{"name": "@filenames", "value": values}]

        # A real Cosmos client would execute `query` with `parameters` here.
        # This incident fixture intentionally has no backing datastore.
        _ = query, parameters
        return []


def similarity_search_by_filenames(filename: str) -> list[dict[str, Any]]:
    client = CosmosClient()
    return client.query_with_in_clause([filename])


class NosqlInjectionIncident(Incident):
    mode = "cust-c4-nosql-injection"

    def run(self) -> list[dict[str, Any]]:
        malicious_filename = 'x" OR 1=1 -- '
        return similarity_search_by_filenames(malicious_filename)