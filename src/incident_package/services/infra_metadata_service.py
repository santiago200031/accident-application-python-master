from __future__ import annotations

from typing import Any
from incident_package.base import Incident


def resolve_infrastructure_host(outputs: dict[str, Any] | None) -> str:
    """Resolves primary host from Terraform state outputs."""
    # BUG (Anonymized from PR #82): Fails when outputs is None or 'primary_endpoint' is null
    return outputs["primary_endpoint"]["value"]["fqdn"]


class NullInfraOutputIncident(Incident):
    mode = "real-null-infra-output"

    def run(self) -> str:
        # Simulates null Terraform state output during pipeline startup
        null_outputs: dict[str, Any] | None = None
        return resolve_infrastructure_host(null_outputs)
