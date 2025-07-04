
# Many Genres

*This model accepts additional fields of type Any.*

## Structure

`ManyGenres`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `genres` | `List[str]` | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "genres": [
    "alternative",
    "samba"
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

