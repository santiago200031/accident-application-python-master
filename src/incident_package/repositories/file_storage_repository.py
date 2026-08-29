from __future__ import annotations

from pathlib import Path
from typing import ClassVar

from incident_package.base import Incident


class MissingFileIncident(Incident):
    mode = "missing-file"
    target_filepath: ClassVar[str] = "data/incident-file.txt"

    def load_configuration_file(self, config_path: str) -> str:
        path = Path(config_path)
        if not path.is_absolute():
            path = Path(__file__).resolve().parents[3] / path

        if not path.is_file():
            return ""

        return path.read_text(encoding="utf-8")

    def run(self) -> str:
        return self.load_configuration_file(self.target_filepath)