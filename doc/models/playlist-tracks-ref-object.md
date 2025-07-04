
# Playlist Tracks Ref Object

*This model accepts additional fields of type Any.*

## Structure

`PlaylistTracksRefObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Optional | A link to the Web API endpoint where full details of the playlist's tracks can be retrieved. |
| `total` | `int` | Optional | Number of tracks in the playlist. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "href": "href0",
  "total": 128,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

