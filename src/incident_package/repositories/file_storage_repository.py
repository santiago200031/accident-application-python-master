from __future__ import annotations

from pathlib import Path
from typing import ClassVar

from incident_package.base import Incident


class MissingFileIncident(Incident):
    mode = "missing-file"
    target_filepath: ClassVar[str] = "data/incident-file.txt"

    def load_configuration_file(self, config_path: str) -> str:
        try:
            return Path(config_path).read_text(encoding="utf-8")
        except FileNotFoundError:
            # A missing runtime artifact is a valid failure mode for this
            # incident. Return a safe empty configuration rather than letting
            # the filesystem exception terminate the run.
            return ""

    def run(self) -> str:
        return self.load_configuration_file(self.target_filepath)