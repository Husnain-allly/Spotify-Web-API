
# Explicit Content Settings Object

*This model accepts additional fields of type Any.*

## Structure

`ExplicitContentSettingsObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter_enabled` | `bool` | Optional | When `true`, indicates that explicit content should not be played. |
| `filter_locked` | `bool` | Optional | When `true`, indicates that the explicit content setting is locked and can't be changed by the user. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "filter_enabled": false,
  "filter_locked": false,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

