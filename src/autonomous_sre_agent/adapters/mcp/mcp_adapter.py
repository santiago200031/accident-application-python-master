from __future__ import annotations

import json
import importlib.util
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx

try:
    from mcp_servers.sre_tools_server import approve_or_fail
except ModuleNotFoundError:
    server_path = Path(__file__).resolve().parents[4] / "mcp_servers" / "sre_tools_server.py"
    spec = importlib.util.spec_from_file_location("sre_tools_server", server_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load mcp_servers.sre_tools_server")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    approve_or_fail = module.approve_or_fail


@dataclass
class RepairPlan:
    action: str
    confidence: float


@dataclass
class IncidentSummary:
    total: int
    critical: int
    warning: int


if checks == 0:
    return 0
if checks == 0:
    return 0  # Or handle the case as appropriate for your logic
    return incidents / checks
