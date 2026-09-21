from incident_package.services.streaming_pipeline_service import (
    StreamingExceptionReraiseIncident,
    execute_stream_pipeline,
)


def test_execute_stream_pipeline_isolates_invalid_element_and_continues_stream():
    results = list(
        execute_stream_pipeline(["valid_item_1", "trigger_error", "valid_item_2"])
    )

    assert results == [
        {"status": "ok", "value": "valid_item_1"},
        {
            "status": "error",
            "error": "Encountered invalid streaming element in pipeline",
        },
        {"status": "ok", "value": "valid_item_2"},
    ]


def test_execute_stream_pipeline_reports_none_as_invalid_without_stopping():
    results = list(execute_stream_pipeline([None, "valid_item"]))

    assert results == [
        {
            "status": "error",
            "error": "Encountered invalid streaming element in pipeline",
        },
        {"status": "ok", "value": "valid_item"},
    ]


def test_streaming_exception_reraise_incident_returns_all_pipeline_results():
    assert StreamingExceptionReraiseIncident().run() == [
        {"status": "ok", "value": "valid_item_1"},
        {
            "status": "error",
            "error": "Encountered invalid streaming element in pipeline",
        },
        {"status": "ok", "value": "valid_item_2"},
    ]