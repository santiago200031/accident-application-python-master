from incident_package.services.user_context_service import NoneDereferenceIncident

def test_retrieve_active_session_count_with_none():
    # Arrange
    incident = NoneDereferenceIncident()
    
    # Act
    result = incident.retrieve_active_session_count(None)
    
    # Assert
    assert result == 0

def test_run_method_with_no_user_session():
    # Arrange
    incident = NoneDereferenceIncident()
    
    # Act
    result = incident.run()
    
    # Assert
    assert result == 0

def test_retrieve_active_session_count_with_valid_session():
    # Arrange
    incident = NoneDereferenceIncident()
    session_context = {"count": 5}
    
    # Act
    result = incident.retrieve_active_session_count(session_context)
    
    # Assert
    assert result == 5

def test_run_method_with_user_session():
    # Arrange
    incident = NoneDereferenceIncident()
    incident._fetch_user_session = lambda: {"count": 3}
    
    # Act
    result = incident.run()
    
    # Assert
    assert result == 3