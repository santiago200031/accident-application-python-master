from incident_package.customer_exceptions.unauthenticated_api import BackendRoutes, UnauthenticatedApiIncident

def test_unauthenticated_api_access():
    # Arrange
    routes = BackendRoutes(auth_enabled=True)

    # Act & Assert
    try:
        routes.list_threads(None)
    except PermissionError as e:
        assert str(e) == "Caller is unauthenticated; access token required for /api/threads"
    else:
        assert False, "PermissionError not raised for unauthenticated access"

def test_authenticated_api_access():
    # Arrange
    routes = BackendRoutes(auth_enabled=True)

    # Act & Assert
    threads = routes.list_threads("valid_token")
    assert threads == [
        {"thread_id": "thread_a1f1c1c8", "project_id": "x", "metadata": {}},
        {"thread_id": "thread_cece7b9f", "project_id": "x", "metadata": {}},
    ]

def test_unauthenticated_api_incident():
    # Arrange
    incident = UnauthenticatedApiIncident()

    # Act & Assert
    result = incident.run()
    assert result == [], "Incident did not handle unauthenticated access gracefully"