from __future__ import annotations

from typing import Any, ClassVar


class Incident:
    mode: ClassVar[str]

    def run(self) -> Any:
        raise NotImplementedError
