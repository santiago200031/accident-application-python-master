from __future__ import annotations

from typing import Any, Generator
from incident_package.base import Incident

def execute_stream_pipeline(items: list[Any]) -> Generator[dict[str, Any], None, None]:
    """Streaming pipeline generator that yields processed items or error chunks."""
    for item in items:
        try:
            if item is None or item == "trigger_error":
                yield {"status": "error", "error": "Encountered invalid streaming element in pipeline"}
            else:
                yield {"status": "ok", "value": item}
        except Exception as exc:
            yield {"status": "error", "error": str(exc)}


class StreamingExceptionReraiseIncident(Incident):
    mode = "real-streaming-reraise"

    def run(self) -> list[dict[str, Any]]:
        pipeline = execute_stream_pipeline(["valid_item_1", "trigger_error", "valid_item_2"])
        return list(pipeline)