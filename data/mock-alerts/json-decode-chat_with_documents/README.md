# json-decode-chat_with_documents

**Exception:** `json.decoder.JSONDecodeError` — unhandled `await req.json()` in `main.py:2241` (`ChatWithDocuments`).

**Cause:** handler parses the request body with no try/except; a malformed JSON body raises
an unhandled exception -> HTTP 500 + `Exception in ASGI application` traceback.

**Fix:** wrap `req.json()` in try/except and return 400.

## WireMock stub (mount in `mappings/json-decode-chat_with_documents.json`)
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
