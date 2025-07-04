
# Too Many Requests Exception

*This model accepts additional fields of type Any.*

## Structure

`TooManyRequestsException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | [`ErrorObject`](../../doc/models/error-object.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "error": {
    "status": 400,
    "message": "message4",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

