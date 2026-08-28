from __future__ import annotations

from incident_package.base import Incident


class NoneDereferenceIncident(Incident):
    mode = "none-dereference"

    def retrieve_active_session_count(self, session_context: dict | None) -> int:
        if session_context is None:
            return 0

        try:
            count = session_context["count"]
        except (KeyError, TypeError):
            return 0

        try:
            return int(count)
        except (TypeError, ValueError):
            return 0

    def run(self) -> int:
        user_session = self._fetch_user_session()
        return self.retrieve_active_session_count(user_session)

    @staticmethod
    def _fetch_user_session() -> dict | None:
        return None