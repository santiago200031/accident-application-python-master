# accident-application-python-master

Intentionally broken UV-based Python app for thesis experiments.

The project now includes real SRE-style methods so an external agent can do non-trivial fixes:
- incident ingestion from JSONL
- risk scoring and action selection
- policy gate decisions
- config patch drafting and write-back
- Git branch creation for remediation work

## Run

```bash
uv run broken-sre-app --mode divide-by-zero
```

## Available failure modes

- `divide-by-zero`: crashes with `ZeroDivisionError`
- `bad-cast`: crashes with `ValueError` on invalid float cast
- `missing-file`: crashes with `FileNotFoundError`
- `index-error`: crashes with `IndexError`
- `network-chaos`: fails on unreachable endpoint / JSON expectations
- `none-dereference`: crashes by indexing into `None`
- `command-injection`: intentionally unsafe shell execution path
- `branch-chaos`: attempts to create an invalid branch name and can fail
- `remediation-workflow`: full workflow (incidents -> policy gate -> config patch -> branch)
- `default`: mixes policy parsing + network path and usually fails

## Real input files used by the workflow

- [config/policy.json](config/policy.json)
- [config/agent.env](config/agent.env)
- [data/incidents.jsonl](data/incidents.jsonl)