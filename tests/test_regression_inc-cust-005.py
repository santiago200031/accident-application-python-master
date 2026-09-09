from incident_package.customer_exceptions.none_dereference_missing_doc import (
    DocumentStore,
    NoneDereferenceMissingDocIncident,
    process_document,
)


def test_process_document_returns_none_when_document_is_missing() -> None:
    store = DocumentStore()

    assert process_document("doc-nonexistent", store) is None


def test_incident_run_handles_missing_document_without_attribute_error() -> None:
    assert NoneDereferenceMissingDocIncident().run() is None


def test_process_document_returns_filename_for_existing_document() -> None:
    assert process_document("doc-existing", DocumentStore()) == "spec.pdf"