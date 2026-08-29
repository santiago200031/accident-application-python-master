import pytest
from incident_package.services.user_context_service import NoneDereferenceIncident

def test_retrieve_active_session_count_with_none():
    # Arrange
    incident = NoneDereferenceIncident()
    
    # Act
    result = incident.retrieve_active_session_count(None)
    
    # Assert
    assert result == 0

def test_run_with_no_user_session():
    # Arrange
    incident = NoneDereferenceIncident()
    
    # Act
    result = incident.run()
    
    # Assert
    assert result == 0

def test_retrieve_active_session_count_with_valid_context():
    # Arrange
    incident = NoneDereferenceIncident()
    session_context = {"count": 5}
    
    # Act
    result = incident.retrieve_active_session_count(session_context)
    
    # Assert
    assert result == 5

def test_run_with_user_session():
    # Arrange
    incident = NoneDereferenceIncident()
    original_fetch_user_session = incident._fetch_user_session
    
    def mock_fetch_user_session() -> dict:
        return {"count": 3}
    
    incident._fetch_user_session = mock_fetch_user_session
    
    # Act
    result = incident.run()
    
    # Assert
    assert result == 3

    # Clean up
    incident._fetch_user_session = original_fetch_user_session