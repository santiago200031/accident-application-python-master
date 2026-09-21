from incident_package.services.infra_metadata_service import resolve_infrastructure_host


def test_resolve_infrastructure_host_returns_empty_string_for_null_endpoint_value():
    outputs = {"primary_endpoint": {"value": None}}

    assert resolve_infrastructure_host(outputs) == ""


def test_resolve_infrastructure_host_returns_empty_string_for_null_primary_endpoint():
    outputs = {"primary_endpoint": None}

    assert resolve_infrastructure_host(outputs) == ""


def test_resolve_infrastructure_host_returns_fqdn_for_valid_terraform_output():
    outputs = {"primary_endpoint": {"value": {"fqdn": "api.example.internal"}}}

    assert resolve_infrastructure_host(outputs) == "api.example.internal"