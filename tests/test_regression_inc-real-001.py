from incident_package.services.streaming_pipeline_service import execute_stream_pipeline

def test_execute_stream_pipeline_with_valid_items():
    items = ["valid_item_1", "valid_item_2"]
    expected_output = [
        {"status": "ok", "value": "valid_item_1"},
        {"status": "ok", "value": "valid_item_2"}
    ]
    output = list(execute_stream_pipeline(items))
    assert output == expected_output

def test_execute_stream_pipeline_with_trigger_error():
    items = ["valid_item_1", "trigger_error", "valid_item_2"]
    expected_output = [
        {"status": "ok", "value": "valid_item_1"},
        {"status": "error", "error": "Encountered invalid streaming element in pipeline"},
        {"status": "ok", "value": "valid_item_2"}
    ]
    output = list(execute_stream_pipeline(items))
    assert output == expected_output

def test_execute_stream_pipeline_with_none_item():
    items = ["valid_item_1", None, "valid_item_2"]
    expected_output = [
        {"status": "ok", "value": "valid_item_1"},
        {"status": "error", "error": "Encountered invalid streaming element in pipeline"},
        {"status": "ok", "value": "valid_item_2"}
    ]
    output = list(execute_stream_pipeline(items))
    assert output == expected_output

def test_execute_stream_pipeline_with_empty_list():
    items = []
    expected_output = []
    output = list(execute_stream_pipeline(items))
    assert output == expected_output