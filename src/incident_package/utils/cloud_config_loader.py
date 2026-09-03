from __future__ import annotations

import os
from typing import Any
from incident_package.base import Incident


def load_cloud_service_config() -> dict[str, Any]:
    """Loads required cloud endpoints and deployment parameters from environment."""
    # BUG (Anonymized from PR #76/#90): Direct subscript access on unset environment variables
    endpoint = os.environ["AZURE_SERVICE_ENDPOINT"]
    api_key = os.environ["AZURE_SERVICE_KEY"]
    return {"endpoint": endpoint, "api_key": api_key}


class MissingConfigEnvironmentIncident(Incident):
    mode = "real-missing-config"

    def run(self) -> dict[str, Any]:
        # Ensures keys are unset to trigger KeyError
        os.environ.pop("AZURE_SERVICE_ENDPOINT", None)
        os.environ.pop("AZURE_SERVICE_KEY", None)
        return load_cloud_service_config()
