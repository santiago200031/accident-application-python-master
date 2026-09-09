# Benchmark Target Service (`accident-application-python-master`)

This repository serves as the intentionally flawed Python microservice used as the empirical evaluation target for the Master's thesis *Safe Autonomous Incident Resolution Agent (SAIRA)*.

It is delivered in its intentionally unpatched baseline state. External autonomous agents inspect the service's runtime error logs, clone the repository, generate tests-first verification suites, synthesize corrective patches, and open pull requests for human review.

---

## 1. Architectural Structure

The service models an asynchronous Python microservice with layered domain responsibilities:

* `src/incident_package/controllers/`: HTTP and event orchestration handlers that dispatch incoming workload requests.
* `src/incident_package/services/`: Business logic, telemetry ingestion, risk scoring, and policy evaluation.
* `src/incident_package/repositories/`: Data access layers, mock database stores, and blob retrieval clients.
* `src/incident_package/utils/`: Shared metric calculators and formatting utilities.
* `src/incident_package/customer_exceptions/`: Anonymized enterprise defect classes derived from live customer environments.
* `tests/`: Automated contract and verification test suites.

---

## 2. Benchmark Scenario Tiers

The repository contains three complementary tiers of intentional software defects:

### Tier 1: Synthetic Faults (`A1` to `A8`)
Exercised through the core CLI entrypoint (`broken-app`) and WireMock observability mocks:
* `inc-2026-001` (`A1`): `ZeroDivisionError` in telemetry metric rate calculations.
* `inc-2026-002` (`A2`): `ValueError` during unvalidated typecasting.
* `inc-2026-003` (`A3`): `FileNotFoundError` when accessing unbundled configuration files.
* `inc-2026-004` (`A4`): `IndexError` during list slicing without boundary validation.
* `inc-2026-005` (`A5`): `httpx.ConnectError` caused by unhandled network connection failures.
* `inc-2026-006` (`A6`): `TypeError` caused by `NoneType` indexing.
* `inc-2026-007` (`A7`): `CalledProcessError` from unsafe shell command execution.
* `inc-2026-008` (`A8`): `KeyError` within pipeline dictionary traversal.

### Tier 2: Real-World Incidents (`R1` to `R8`)
Derived from historical systems engineering copilot telemetry (PRs #67 through #110):
* `inc-real-001` (`R1`): Bare `raise` in streaming generator propagating handled errors.
* `inc-real-002` (`R2`): Blob container creation conflict on existing cloud storage resources.
* `inc-real-003` (`R3`): Queue PDF trigger crash on non-JSON payloads without dead-letter guards.
* `inc-real-004` (`R4`): Missing cloud environment configuration fallback defaults.
* `inc-real-005` (`R5`): Null infrastructure output pointer dereference in Terraform metadata resolvers.
* `inc-real-006` (`R6`): Remediation loop duplicate state suppression and 422 HTTP conflicts.
* `inc-real-007` (`R7`): Service error boundary failure in inbound API endpoints.
* `inc-real-008` (`R8`): Zero denominator in metric rate calculations.

### Tier 3: Customer Exceptions (`C1` to `C6`)
Anonymized defect patterns distilled from live enterprise microservice operations:
* `inc-cust-001` (`C1`): Missing caller authentication token enforcement across API routes.
* `inc-cust-002` (`C2`): Unguarded `json.loads()` raising unhandled `JSONDecodeError` exceptions.
* `inc-cust-003` (`C3`): Path traversal and Insecure Direct Object Reference (IDOR) in blob retrieval.
* `inc-cust-004` (`C4`): Cosmos NoSQL query injection via unparameterized string concatenation.
* `inc-cust-005` (`C5`): `NoneType` attribute access when documents are missing from the store.
* `inc-cust-006` (`C6`): Alert rules scoped to inactive Application Insights telemetry sinks.

---

## 3. Setup and Execution

### Prerequisites
* Python 3.12 or 3.13
* `uv` package manager

### Running Failure Modes via CLI
Individual synthetic faults can be executed directly:
```bash
uv run broken-app --mode divide-by-zero
uv run broken-app --mode bad-cast
uv run broken-app --mode network-chaos
uv run broken-app --mode remediation-workflow
```

### Running Test Suites
1. **Verify Baseline Fault Presence:**
   Tests in `test_placeholder.py` assert that the unpatched repository raises the expected exceptions:
   ```bash
   uv run pytest tests/test_placeholder.py
   ```
   All 8 tests pass on the baseline code, confirming that intentional faults are present.

2. **Run Autonomous Agent Contract Tests:**
   Contract tests specify the required post-fix behavior. In the baseline repository, these fail out of the box:
   ```bash
   uv run pytest tests/test_real_scenarios.py tests/test_customer_exceptions.py
   ```
   An autonomous remediation agent must repair the underlying source files until all contract tests pass cleanly without regressions.