# process_document-not-found

**Exception:** Cosmos DB `NotFound` — `process_document` calls `.get()` on `None` when
`get_doc_int_result()` returns no document (`document_request.py:291`).

**Fix:** guard against `None` and return 404.

## WireMock stub (mount in `mappings/process_document-not-found.json`)
```json
{
  "request": {
    "method": "POST",
    "urlPath": "/alerts/log-analytics"
  },
  "response": {
    "status": 200,
    "headers": { "Content-Type": "application/json" },
    "body": ""
  }
}
```
`payload.json` is the request body Azure Monitor POSTs to your agent (Common Alert Schema).
Feed it to your agent handler directly, or use WireMock's `bodyPatterns`/`contains`
matcher to replay this exact payload to `POST /alerts/log-analytics`.
