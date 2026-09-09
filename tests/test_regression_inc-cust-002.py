from incident_package.customer_exceptions.malformed_json_body import (
    query_requirements_http,
    delete_documents_http,
)

def test_query_requirements_http_malformed_json():
    # Test case for the original bug scenario
    bad_body = '{"query": "x", "project_id": "x"'
    response = query_requirements_http(bad_body)
    assert response == {"status": 400, "message": "Malformed JSON body"}

def test_delete_documents_http_malformed_json():
    # Test case for the original bug scenario on the second endpoint
    bad_body = '{"partition_key": "x", "document_id": "x"'
    response = delete_documents_http(bad_body)
    assert response == {"status": 400, "message": "Malformed JSON body"}

def test_query_requirements_http_valid_json():
    # Test case for valid JSON input
    good_body = '{"query": "x", "project_id": "x"}'
    response = query_requirements_http(good_body)
    assert response == {"status": 200, "query": "x"}

def test_delete_documents_http_valid_json():
    # Test case for valid JSON input on the second endpoint
    good_body = '{"partition_key": "x", "document_id": "x"}'
    response = delete_documents_http(good_body)
    assert response == {"status": 200, "partition_key": "x"}