from __future__ import annotations

from incident_package.base import Incident


class IndexErrorIncident(Incident):
    mode = "index-error"

    def fetch_record_at_index(self, records_list: list[str], target_index: int) -> str:
        total_records = len(records_list)
        normalized_index = (
            target_index
            if target_index >= 0
            else total_records + target_index
        )
        if normalized_index < 0 or normalized_index >= total_records:
            return ""
        return records_list[normalized_index]

    def run(self) -> str:
        active_records = ["only-one"]
        requested_index = 10
        return self.fetch_record_at_index(active_records, requested_index)