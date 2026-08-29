from __future__ import annotations

from incident_package.base import Incident


class BadCastIncident(Incident):
    mode = "bad-cast"

    def parse_float_setting(self, raw_input_str: str) -> float:
        try:
            return float(raw_input_str)
        except (ValueError, TypeError):
            return 0.0

    def run(self) -> float:
        unparsed_setting = "not-a-number"
        return self.parse_float_setting(unparsed_setting)