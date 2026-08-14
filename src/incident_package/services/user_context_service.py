from __future__ import annotations

from incident_package.base import Incident


class NoneDereferenceIncident(Incident):
    mode = "none-dereference"

    def retrieve_active_session_count(self, session_context: dict | None) -> int:
        return session_context["count"]

    def run(self) -> int:
        user_session = self._fetch_user_session()
        return self.retrieve_active_session_count(user_session)

    @staticmethod
    def _fetch_user_session() -> dict | None:
        return None
