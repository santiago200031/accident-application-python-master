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
            payload = response.json()
        except (httpx.HTTPError, ValueError):
            return {}

        return payload if isinstance(payload, dict) else {}

    def run(self) -> dict:
        return self.fetch_remote_payload(self.endpoint_url)