from __future__ import annotations

from incident_package.base import Incident


class NoneDereferenceIncident(Incident):
    mode = "none-dereference"

    def retrieve_active_session_count(self, session_context: dict | None) -> int:
        if not isinstance(session_context, dict):
            return 0

        count = session_context.get("count", 0)
        return count if isinstance(count, int) else 0

    def run(self) -> int:
        user_session = self._fetch_user_session()
        return self.retrieve_active_session_count(user_session)

    @staticmethod
    def _fetch_user_session() -> dict | None:
        return None