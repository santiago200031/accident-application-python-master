from __future__ import annotations

from typing import ClassVar, Dict

import httpx

from incident_package.base import Incident

class NetworkChaosIncident(Incident):
    mode = "network-chaos"
    endpoint_url: ClassVar[str] = "http://127.0.0.1:9/nowhere"

    def fetch_remote_payload(self, target_url: str) -> Dict:
        try:
            response = httpx.get(target_url, timeout=0.5)
            return response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as e:
            print(f"Failed to fetch remote payload: {e}")
            return {}

    def run(self) -> Dict:
        return self.fetch_remote_payload(self.endpoint_url)