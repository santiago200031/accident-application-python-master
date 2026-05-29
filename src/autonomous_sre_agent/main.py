from __future__ import annotations

import argparse

# TODO: Install the 'autonomous_sre_agent' module if it's not already installed.
from autonomous_sre_agent.adapters.mcp.mcp_adapter import BrokenMCPAdapter


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Intentionally broken external software for thesis experiments"
    )
    parser.add_argument(
        "--mode",
        default="default",
        choices=[
            "default",
            "divide-by-zero",
            "bad-cast",
            "missing-file",
            "index-error",
            "network-chaos",
            "none-dereference",
            "command-injection",
            "branch-chaos",
            "remediation-workflow",
        ],
        help="Select which failure mode to execute",
    )
    parser.add_argument(
        "--policy-path",
        default="config/policy.json",
        help="Path to policy file, often intentionally missing in this project",
    )
    return parser


def cli() -> None:
    args = build_parser().parse_args()
    adapter = BrokenMCPAdapter(policy_path=args.policy_path)
    result = adapter.execute(mode=args.mode)
    print("RESULT:", result)


if __name__ == "__main__":
    cli()
