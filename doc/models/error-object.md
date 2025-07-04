
# Error Object

*This model accepts additional fields of type Any.*

## Structure

`ErrorObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `int` | Required | The HTTP status code (also returned in the response header; see [Response Status Codes](/documentation/web-api/concepts/api-calls#response-status-codes) for more information).<br><br>**Constraints**: `>= 400`, `<= 599` |
| `message` | `str` | Required | A short description of the cause of the error. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "status": 400,
  "message": "message8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

