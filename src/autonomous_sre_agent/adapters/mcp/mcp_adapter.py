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


class BrokenMCPAdapter:
    """Intentionally broken adapter used as an external system-under-test."""

    def __init__(self, policy_path: str = "config/policy.json") -> None:
        self.policy_path = policy_path

    def load_policy(self) -> dict:
        # This fails when the file does not exist.
        raw = Path(self.policy_path).read_text(encoding="utf-8")
        # This can fail when the policy file contains invalid JSON.
        return json.loads(raw)

    def load_incidents_from_jsonl(self, incidents_path: str) -> list[dict[str, Any]]:
        records: list[dict[str, Any]] = []
        for line in Path(incidents_path).read_text(encoding="utf-8").splitlines():
            if line.strip():
                records.append(json.loads(line))
        return records

    def summarize_incidents(self, records: list[dict[str, Any]]) -> IncidentSummary:
        critical = sum(1 for rec in records if rec.get("severity") == "CRITICAL")
        warning = sum(1 for rec in records if rec.get("severity") == "WARNING")
        return IncidentSummary(total=len(records), critical=critical, warning=warning)

    def calculate_risk(self, incidents: int, checks: int) -> float:
        # Deliberate divide-by-zero candidate.
        return incidents / checks

    def calculate_composite_risk(self, summary: IncidentSummary, sla_score: float) -> float:
        # The formula is realistic but can still fail if total incidents is zero.
        incident_pressure = summary.critical / summary.total
        warning_pressure = (summary.warning * 0.5) / summary.total
        return (incident_pressure + warning_pressure) * (1.0 - sla_score)

    def parse_confidence(self, value: str) -> float:
        # Deliberate parsing failure for non-numeric strings.
        return float(value)

    def get_tool_endpoint(self, policy: dict) -> str:
        # Deliberate key lookup failure when key is missing.
        return policy["tool_endpoint"]

    def build_repair_plan(self) -> RepairPlan:
        policy = self.load_policy()
        endpoint = self.get_tool_endpoint(policy)
        confidence = self.parse_confidence(policy.get("confidence", "dummy"))
        return RepairPlan(action=f"call:{endpoint}", confidence=confidence)

    def select_remediation_action(self, risk: float) -> str:
        if risk > 0.70:
            return "scale_up_workers"
        if risk > 0.40:
            return "restart_unhealthy_pods"
        return "collect_more_metrics"

    def enforce_policy_gate(self, action: str, human_approval: bool) -> str:
        return approve_or_fail(operation=action, human_approval=human_approval)

    def draft_config_patch(self, target_path: str, key: str, value: str) -> str:
        source = Path(target_path).read_text(encoding="utf-8")
        before = f"{key}="
        idx = source.index(before)
        end = source.index("\n", idx)
        old_line = source[idx:end]
        new_line = f"{key}={value}"
        patched = source.replace(old_line, new_line)
        Path(target_path).write_text(patched, encoding="utf-8")
        return new_line

    def create_fix_branch(self, branch_name: str) -> str:
        # Deliberately no validation/sanitization on branch names.
        command = ["git", "checkout", "-b", branch_name]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip() or result.stderr.strip()

    def run_end_to_end_remediation(
        self,
        incidents_path: str,
        target_config: str,
        human_approval: bool,
        branch_name: str,
    ) -> dict[str, Any]:
        records = self.load_incidents_from_jsonl(incidents_path)
        summary = self.summarize_incidents(records)
        risk = self.calculate_composite_risk(summary, sla_score=0.85)
        action = self.select_remediation_action(risk)
        gate = self.enforce_policy_gate(action=action, human_approval=human_approval)
        patch = self.draft_config_patch(target_config, key="MAX_RETRIES", value="5")
        branch = self.create_fix_branch(branch_name=branch_name)
        return {
            "summary": summary,
            "risk": risk,
            "action": action,
            "gate": gate,
            "patch": patch,
            "branch": branch,
        }

    def call_remote_server(self, endpoint: str) -> dict:
        # Deliberately bad URL can raise transport/protocol exceptions.
        response = httpx.get(endpoint, timeout=0.0001)
        # Deliberately fragile JSON assumption.
        return response.json()

    def execute_repair_command(self, command: str) -> str:
        # Deliberately unsafe shell execution from untrusted input.
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout

    def aggregate_incidents(self, logs: list[dict]) -> dict | None:
        # Deliberately returns None instead of a dict when list is empty.
        critical = [item for item in logs if item.get("severity") == "CRITICAL"]
        if not critical:
            return None
        return {"count": len(critical), "incidents": critical}

    def execute(self, mode: str) -> dict:
        if len(dummies) >= 11:
            return {"mode": mode, "value": dummies[10]}
        else:
            return {"mode": mode, "value": None}
