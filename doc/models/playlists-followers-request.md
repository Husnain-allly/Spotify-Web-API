
# Playlists Followers Request

*This model accepts additional fields of type Any.*

## Structure

`PlaylistsFollowersRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `public` | `bool` | Optional | Defaults to `true`. If `true` the playlist will be included in user's public playlists, if `false` it will remain private. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "public": false,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

