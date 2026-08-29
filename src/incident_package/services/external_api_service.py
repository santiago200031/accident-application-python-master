from __future__ import annotations

from typing import ClassVar

import httpx

from incident_package.base import Incident
class NetworkChaosIncident(Incident):
    mode = "network-chaos"
    endpoint_url: ClassVar[str] = "http://127.0.0.1:9/nowhere"

    def fetch_remote_payload(self, target_url: str) -> dict:
        try:
            response = httpx.get(target_url, timeout=0.5)
            return response.json()
        except httpx.ConnectError:
            # Handle connection refusal gracefully by returning an empty dictionary
            return {}

    def run(self) -> dict:
        return self.fetch_remote_payload(self.endpoint_url)