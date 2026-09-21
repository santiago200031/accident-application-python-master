from __future__ import annotations

import os
from typing import Any

from incident_package.base import Incident


def load_cloud_service_config() -> dict[str, Any]:
    """Loads cloud endpoints and deployment parameters from the environment.

    Missing configuration values are represented by empty strings so callers can
    handle unavailable Azure configuration without an environment lookup failure.
    """
    endpoint = os.environ.get("AZURE_SERVICE_ENDPOINT", "")
    api_key = os.environ.get("AZURE_SERVICE_KEY", "")
    return {"endpoint": endpoint, "api_key": api_key}


class MissingConfigEnvironmentIncident(Incident):
    mode = "real-missing-config"

    def run(self) -> dict[str, Any]:
        # Ensures keys are unset to verify missing configuration is handled safely.
        os.environ.pop("AZURE_SERVICE_ENDPOINT", None)
        os.environ.pop("AZURE_SERVICE_KEY", None)
        return load_cloud_service_config()