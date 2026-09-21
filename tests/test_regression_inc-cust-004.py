from incident_package.customer_exceptions import nosql_injection


def test_similarity_search_passes_malicious_filename_as_single_list_value(monkeypatch):
    malicious_filename = 'x" OR 1=1 -- '
    received = {}

    class RecordingCosmosClient:
        def query_with_in_clause(self, filenames):
            received["filenames"] = filenames
            return [{"document_filename": malicious_filename}]

    monkeypatch.setattr(nosql_injection, "CosmosClient", RecordingCosmosClient)

    result = nosql_injection.similarity_search_by_filenames(malicious_filename)

    assert received["filenames"] == [malicious_filename]
    assert result == [{"document_filename": malicious_filename}]


def test_cosmos_client_accepts_sql_looking_filename_without_malformed_query_error():
    malicious_filename = 'report.pdf") OR 1=1 -- '

    result = nosql_injection.CosmosClient().query_with_in_clause(
        [malicious_filename, "normal.pdf"]
    )

    assert result == []


def test_cosmos_client_rejects_empty_or_non_string_filename_collections():
    client = nosql_injection.CosmosClient()

    assert client.query_with_in_clause([]) == []
    assert client.query_with_in_clause(["valid.pdf", ""]) == []
    assert client.query_with_in_clause(["valid.pdf", None]) == []
    assert client.query_with_in_clause({"valid.pdf"}) == []