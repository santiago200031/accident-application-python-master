from __future__ import annotations

import math

from incident_package.base import Incident


class BadCastIncident(Incident):
    mode = "bad-cast"

    def parse_float_setting(self, raw_input_str: str) -> float:
        """Parse a float setting, using 0.0 for invalid input."""
        try:
            value = float(raw_input_str)
        except (TypeError, ValueError):
            return 0.0

        return value if math.isfinite(value) else 0.0

    def run(self) -> float:
        unparsed_setting = "not-a-number"
        return self.parse_float_setting(unparsed_setting)