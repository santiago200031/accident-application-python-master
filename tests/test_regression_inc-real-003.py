import pytest
from incident_package.controllers.queue_consumer_controller import process_queue_message

def test_process_queue_message_valid_json():
    # Arrange
    valid_payload = '{"message_id": 123, "payload": "valid data"}'
    
    # Act
    result = process_queue_message(valid_payload)
    
    # Assert
    assert result == {"status": "processed", "id": 123, "body": "valid data"}

def test_process_queue_message_invalid_json():
    # Arrange
    invalid_payload = "CORRUPTED_NON_JSON_DATA_STREAM_##!"
    
    # Act
    result = process_queue_message(invalid_payload)
    
    # Assert
    assert result == {"status": "error", "id": 0, "body": "Invalid JSON payload"}

def test_process_queue_message_empty_string():
    # Arrange
    empty_payload = ""
    
    # Act
    result = process_queue_message(empty_payload)
    
    # Assert
    assert result == {"status": "error", "id": 0, "body": "Invalid JSON payload"}

def test_process_queue_message_malformed_json():
    # Arrange
    malformed_payload = '{"message_id": 123, "payload": "valid data"'
    
    # Act
    result = process_queue_message(malformed_payload)
    
    # Assert
    assert result == {"status": "error", "id": 0, "body": "Invalid JSON payload"}