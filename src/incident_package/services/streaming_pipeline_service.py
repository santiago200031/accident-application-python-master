from __future__ import annotations

from typing import Any, Generator

from incident_package.base import Incident


def execute_stream_pipeline(items: list[Any]) -> Generator[dict[str, Any], None, None]:
    """Yield processed items and safely report invalid items without stopping the stream."""
    for item in items:
        try:
            if item is None or item == "trigger_error":
                raise ValueError("Encountered invalid streaming element in pipeline")
            yield {"status": "ok", "value": item}
        except ValueError as exc:
            # Invalid input is isolated to this item so later stream elements remain usable.
            yield {"status": "error", "error": str(exc)}


class StreamingExceptionReraiseIncident(Incident):
    mode = "real-streaming-reraise"

    def run(self) -> list[dict[str, Any]]:
        pipeline = execute_stream_pipeline(["valid_item_1", "trigger_error", "valid_item_2"])
        return list(pipeline)