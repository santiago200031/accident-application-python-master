from __future__ import annotations

default_value = 0.0

class BadCastIncident:
    def parse_float_setting(self, raw_input_str: str) -> float:
        try:
            return float(raw_input_str)
        except ValueError:
            return default_value

    def run(self) -> float:
        unparsed_setting = "not-a-number"
        return self.parse_float_setting(unparsed_setting)