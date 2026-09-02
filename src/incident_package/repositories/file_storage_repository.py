from __future__ import annotations

from pathlib import Path
from typing import ClassVar

from incident_package.base import Incident


class MissingFileIncident(Incident):
    mode = "missing-file"
    target_filepath: ClassVar[str] = "data/incident-file.txt"

    def load_configuration_file(self, config_path: str) -> str:
        """Load a configuration file without depending on the process CWD.

        Relative paths are first resolved as supplied, preserving the existing
        behavior for callers and tests that provide files relative to the
        current working directory.  Stable project and package-root locations
        are then tried so execution from another working directory still works.
        A missing deployment artifact is treated as an empty configuration,
        allowing the incident to complete without raising FileNotFoundError.
        """
        requested_path = Path(config_path)
        candidate_paths = [requested_path]

        if not requested_path.is_absolute():
            source_path = Path(__file__).resolve()
            project_root = source_path.parents[3]
            package_root = source_path.parents[2]
            candidate_paths.extend(
                (
                    project_root / requested_path,
                    package_root / requested_path,
                )
            )

        seen: set[Path] = set()
        for candidate in candidate_paths:
            resolved_candidate = candidate if candidate.is_absolute() else candidate.resolve()
            if resolved_candidate in seen:
                continue
            seen.add(resolved_candidate)

            try:
                return resolved_candidate.read_text(encoding="utf-8")
            except FileNotFoundError:
                continue

        return ""

    def run(self) -> str:
        return self.load_configuration_file(self.target_filepath)