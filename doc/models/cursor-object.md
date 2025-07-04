
# Cursor Object

*This model accepts additional fields of type Any.*

## Structure

`CursorObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `after` | `str` | Optional | The cursor to use as key to find the next page of items. |
| `before` | `str` | Optional | The cursor to use as key to find the previous page of items. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "after": "after2",
  "before": "before0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

