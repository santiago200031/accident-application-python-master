from __future__ import annotations

import json
from typing import Any
from incident_package.base import Incident


def process_queue_message(raw_payload: str) -> dict[str, Any]:
    """Parses incoming message from storage queue without schema validation."""
    # BUG (Anonymized from PR #79/#81): Missing exception guard against corrupted/non-JSON queue payloads
    parsed = json.loads(raw_payload)
    return {"status": "processed", "id": parsed["message_id"], "body": parsed["payload"]}


class MalformedQueuePayloadIncident(Incident):
    mode = "real-malformed-queue"

    def run(self) -> dict[str, Any]:
        # Simulates corrupted queue message (e.g. non-JSON text or malformed PDF trigger)
        corrupted_payload = "CORRUPTED_NON_JSON_DATA_STREAM_##!"
        return process_queue_message(corrupted_payload)
