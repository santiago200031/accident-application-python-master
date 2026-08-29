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
            project_root = Path(__file__).resolve().parents[3]
            project_relative_path = project_root / path
            if project_relative_path.is_file():
                path = project_relative_path

        if not path.is_file():
            return ""

        try:
            return path.read_text(encoding="utf-8")
        except OSError:
            return ""

    def run(self) -> str:
        return self.load_configuration_file(self.target_filepath)