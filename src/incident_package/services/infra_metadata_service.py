from __future__ import annotations

from typing import Any

from incident_package.base import Incident


def resolve_infrastructure_host(outputs: dict[str, Any] | None) -> str:
    """Resolve the primary host from Terraform state outputs.

    Returns an empty string when Terraform has not produced a usable primary
    endpoint yet, such as during pipeline startup or optional provisioning.
    """
    if not isinstance(outputs, dict):
        return ""

    primary_endpoint = outputs.get("primary_endpoint")
    if not isinstance(primary_endpoint, dict):
        return ""

    value = primary_endpoint.get("value")
    if not isinstance(value, dict):
        return ""

    fqdn = value.get("fqdn")
    return fqdn if isinstance(fqdn, str) else ""


class NullInfraOutputIncident(Incident):
    mode = "real-null-infra-output"

    def run(self) -> str:
        # Simulates null Terraform state output during pipeline startup
        null_outputs: dict[str, Any] | None = None
        return resolve_infrastructure_host(null_outputs)