from __future__ import annotations

from incident_package.base import Incident


class IndexErrorIncident(Incident):
    mode = "index-error"

    def fetch_record_at_index(self, records_list: list[str], target_index: int) -> str:
        if target_index < 0 or target_index >= len(records_list):
            return ""
        return records_list[target_index]

    def run(self) -> str:
        active_records = ["only-one"]
        requested_index = 10
        return self.fetch_record_at_index(active_records, requested_index)