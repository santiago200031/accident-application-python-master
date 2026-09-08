# Mock Alert Payloads (for WireMock / local agent testing)

One folder per exception. Each contains `payload.json` — the **request body Azure
Monitor POSTs to your SRE agent** (Common Alert Schema, `useCommonAlertSchema: true`),
as delivered to `POST /alerts/log-analytics` via action group `ag-custa-log-analytics`.

Use these to wiremock the alert webhook and replay each exception against your agent
locally (no live Azure needed).

## Structure
```
mock-alerts/
  <exception>/payload.json   # Common Alert Schema webhook body
  <exception>/README.md      # what it is + WireMock stub snippet
```

## Exceptions covered
| Folder | Exception | Root cause |
|--------|-----------|------------|
| `json-decode-query_requirements` | JSONDecodeError | `main.py:2138` no try/except on `req.json()` |
| `json-decode-delete_documents` | JSONDecodeError | `main.py:1666` |
| `json-decode-chat_with_documents` | JSONDecodeError | `main.py:2241` |
| `json-decode-get_segments_by_document` | JSONDecodeError | `main.py:2216` |
| `json-decode-update_segment` | JSONDecodeError | `main.py:1694` |
| `json-decode-get_requirements_by_filename` | JSONDecodeError | `main.py:2164` |
| `nosql-injection-get_requirements_by_filename` | Cosmos BadRequest | `raise_cosmosdb_client.py:577-578` |
| `process_document-not-found` | Cosmos NotFound (None deref) | `document_request.py:291` |

## Schema notes
- `schemaId`: `azureMonitorCommonAlertSchema`.
- `data.essentials`: rule metadata (`alertRule`, `severity`, `monitorCondition`,
  `monitoringService: "Log Alerts V2"`, `alertTargetIDs`).
- `data.alertContext.properties.customProperties`: `service_id` and `log_level`
  set on the action-group rule.
- `data.alertContext.condition`: the LogQueryCriteria (searchQuery, window, metricValue).
- `alertSearchResults.tables[0].rows`: the actual log rows (TimeGenerated, Message, Source)
  for the exception. (Real Azure payload may summarize counts — the agent normally
  re-runs the query via `linkToSearchResultsAPI` to fetch raw rows.)

## Endpoints (action groups → agent)
| Endpoint | Action group | Alert rule |
|----------|--------------|-----------|
| `/alerts/log-analytics` | `ag-custa-log-analytics` | `alert-custa-loganalytics-errors` (5m) + `custa-exceptions-errors-hourly` (1h scheduler) |
| `/alerts/app-insights` | `ag-custa-app-insights` | `custa-all-exceptions` (dead — empty App Insights) |
| `/alerts/azure-monitor` | `ag-custa-azure-monitor` + `ag-custa-prod` | `alert-custa-azuremonitor-errors` (dead) |

The 1h scheduler (`custa-exceptions-errors-hourly`) produces the same Common Alert
Schema, only `condition.windowSize = "PT1H"` and the query bins by `1h`.

## WireMock quick start
1. Run WireMock: `java -jar wiremock.jar --port 8000`.
2. Mount a stub (per-folder `README.md`) for `POST /alerts/log-analytics`.
3. Point your agent at `http://localhost:8000` and replay `payload.json`.
