
# Simplified Artist Object

*This model accepts additional fields of type Any.*

## Structure

`SimplifiedArtistObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `external_urls` | [`ExternalUrlObject`](../../doc/models/external-url-object.md) | Optional | Known external URLs for this artist. |
| `href` | `str` | Optional | A link to the Web API endpoint providing full details of the artist. |
| `id` | `str` | Optional | The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the artist. |
| `name` | `str` | Optional | The name of the artist. |
| `mtype` | [`Type`](../../doc/models/type.md) | Optional | The object type. |
| `uri` | `str` | Optional | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the artist. |
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
  "href": "href6",
  "id": "id4",
  "name": "name4",
  "type": "artist",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

