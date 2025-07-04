
# External Url Object

*This model accepts additional fields of type Any.*

## Structure

`ExternalUrlObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `spotify` | `str` | Optional | The [Spotify URL](/documentation/web-api/concepts/spotify-uris-ids) for the object. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "spotify": "spotify4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

