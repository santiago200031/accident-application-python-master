from __future__ import annotations

from pathlib import Path
from typing import ClassVar

class Incident:
    pass

class MissingFileIncident(Incident):
    mode = "missing-file"
    target_filepath: ClassVar[str] = "data/incident-file.txt"

    def load_configuration_file(self, config_path: str) -> str:
        path = Path(config_path)
        if not path.exists():
            return ""
        return path.read_text(encoding="utf-8")

    def run(self) -> str:
        return self.load_configuration_file(self.target_filepath)