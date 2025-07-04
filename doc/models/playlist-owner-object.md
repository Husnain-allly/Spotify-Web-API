
# Playlist Owner Object

*This model accepts additional fields of type Any.*

## Structure

`PlaylistOwnerObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `external_urls` | [`ExternalUrlObject`](../../doc/models/external-url-object.md) | Optional | Known public external URLs for this user. |
| `followers` | [`FollowersObject`](../../doc/models/followers-object.md) | Optional | Information about the followers of this user. |
| `href` | `str` | Optional | A link to the Web API endpoint for this user. |
| `id` | `str` | Optional | The [Spotify user ID](/documentation/web-api/concepts/spotify-uris-ids) for this user. |
| `mtype` | [`Type3`](../../doc/models/type-3.md) | Optional | The object type. |
| `uri` | `str` | Optional | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for this user. |
| `display_name` | `str` | Optional | The name displayed on the user's profile. `null` if not available. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "external_urls": {
    "spotify": "spotify6",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "followers": {
    "href": "href0",
    "total": 82,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "href": "href4",
  "id": "id2",
  "type": "user",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

