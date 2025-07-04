
# Context Object

*This model accepts additional fields of type Any.*

## Structure

`ContextObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | The object type, e.g. "artist", "playlist", "album", "show". |
| `href` | `str` | Optional | A link to the Web API endpoint providing full details of the track. |
| `external_urls` | [`ExternalUrlObject`](../../doc/models/external-url-object.md) | Optional | External URLs for this context. |
| `uri` | `str` | Optional | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the context. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "type": "type6",
  "href": "href6",
  "external_urls": {
    "spotify": "spotify6",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "uri": "uri8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

