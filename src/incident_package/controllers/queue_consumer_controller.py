from __future__ import annotations

import json
from typing import Any

from incident_package.base import Incident


def process_queue_message(raw_payload: str) -> dict[str, Any]:
    """Parse an incoming queue message, safely rejecting invalid payloads."""
    if not isinstance(raw_payload, str) or not raw_payload.strip():
        return {"status": "invalid"}

    try:
        parsed = json.loads(raw_payload)
    except (json.JSONDecodeError, TypeError):
        return {"status": "invalid"}

    if not isinstance(parsed, dict):
        return {"status": "invalid"}

    try:
        message_id = parsed["message_id"]
        body = parsed["payload"]
    except KeyError:
        return {"status": "invalid"}

    return {"status": "processed", "id": message_id, "body": body}


class MalformedQueuePayloadIncident(Incident):
    mode = "real-malformed-queue"

    def run(self) -> dict[str, Any]:
        # Simulates corrupted queue message (e.g. non-JSON text or malformed PDF trigger)
        corrupted_payload = "CORRUPTED_NON_JSON_DATA_STREAM_##!"
        return process_queue_message(corrupted_payload)