# nosql-injection-get_requirements_by_filename

**Exception:** Cosmos DB `BadRequest` — SQL `IN` clause built via raw string interpolation of `filenames`
(`raise_cosmosdb_client.py:577-578`) and a `filename` string iterated as a list.

**Fix:** use a parameterized `@filenames` array and pass a list.

## WireMock stub (mount in `mappings/nosql-injection-get_requirements_by_filename.json`)
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
