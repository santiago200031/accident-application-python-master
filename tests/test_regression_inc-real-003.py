import pytest

from incident_package.controllers.queue_consumer_controller import (
    MalformedQueuePayloadIncident,
    process_queue_message,
)


@pytest.mark.parametrize(
    "raw_payload",
    [
        "",
        "   ",
        "CORRUPTED_NON_JSON_DATA_STREAM_##!",
        "{'message_id': 'msg-1', 'payload': 'invalid single-quoted json'}",
        "{",
        "null",
        "[]",
        '"plain string"',
        "123",
    ],
)
def test_process_queue_message_rejects_empty_malformed_and_non_object_payloads(
    raw_payload,
):
    assert process_queue_message(raw_payload) == {"status": "invalid"}


@pytest.mark.parametrize("raw_payload", [None, 42, {}, []])
def test_process_queue_message_rejects_non_string_payloads(raw_payload):
    assert process_queue_message(raw_payload) == {"status": "invalid"}


@pytest.mark.parametrize(
    "raw_payload",
    [
        "{}",
        '{"message_id": "message-1"}',
        '{"payload": {"event": "created"}}',
    ],
)
def test_process_queue_message_rejects_objects_missing_required_fields(raw_payload):
    assert process_queue_message(raw_payload) == {"status": "invalid"}


def test_process_queue_message_processes_valid_queue_payload():
    payload = '{"message_id": "message-123", "payload": {"event": "created"}}'

    assert process_queue_message(payload) == {
        "status": "processed",
        "id": "message-123",
        "body": {"event": "created"},
    }


def test_malformed_queue_payload_incident_returns_controlled_invalid_outcome():
    assert MalformedQueuePayloadIncident().run() == {"status": "invalid"}