from __future__ import annotations

from typing import Any
from incident_package.base import Incident


class DocumentStore:
    """Cosmos-backed document store that returns None for missing docs."""

    def __init__(self) -> None:
        self.documents: dict[str, dict[str, Any]] = {
            "doc-existing": {"filename": "spec.pdf", "project_id": "x"}
        }

    def get_doc_int_result(self, document_id: str) -> dict[str, Any] | None:
        return self.documents.get(document_id)


def process_document(document_id: str, store: DocumentStore) -> str:
    doc = store.get_doc_int_result(document_id)
    # BUG (Anonymized C5): direct .get("filename") on a possibly-None result
    return doc.get("filename")


class NoneDereferenceMissingDocIncident(Incident):
    mode = "cust-c5-none-deref-missing-doc"

    def run(self) -> str:
        store = DocumentStore()
        # document_id does not exist -> get_doc_int_result returns None
        return process_document("doc-nonexistent", store)
