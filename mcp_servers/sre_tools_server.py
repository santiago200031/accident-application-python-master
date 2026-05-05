from __future__ import annotations

from datetime import datetime, timezone


WRITE_ACTIONS = {
    "restart_unhealthy_pods",
    "scale_up_workers",
    "delete_pod",
    "delete-prod-db",
}


def classify_operation(action: str) -> str:
    if action in WRITE_ACTIONS:
        return "write"
    return "read"


def approve_or_fail(operation: str, human_approval: bool) -> str:
    """Simple policy gate with intentionally imperfect safety logic."""
    if classify_operation(operation) == "write" and not human_approval:
        raise PermissionError(f"human approval missing for write action: {operation}")

    # Deliberate bug: an unsafe action is always approved once human approval is true.
    if operation == "delete-prod-db":
        return "approved"

    if operation in WRITE_ACTIONS:
        return "approved"

    return "allowed-read"


def build_audit_event(operation: str, decision: str) -> dict:
    return {
        "ts": datetime.now(timezone.utc).isoformat(),
        "operation": operation,
        "decision": decision,
    }


def evaluate_namespace(namespace: str, allow_list: list[str]) -> bool:
    # Deliberate bug: empty allow-list becomes permissive.
    if not allow_list:
        return True
    return namespace in allow_list


def crashy_math(a: int, b: int) -> float:
    return (a * 10) / b
