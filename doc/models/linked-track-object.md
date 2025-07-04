
# Linked Track Object

*This model accepts additional fields of type Any.*

## Structure

`LinkedTrackObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `external_urls` | [`ExternalUrlObject`](../../doc/models/external-url-object.md) | Optional | Known external URLs for this track. |
| `href` | `str` | Optional | A link to the Web API endpoint providing full details of the track. |
| `id` | `str` | Optional | The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the track. |
| `mtype` | `str` | Optional | The object type: "track". |
| `uri` | `str` | Optional | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the track. |
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
  "href": "href0",
  "id": "id8",
  "type": "type2",
  "uri": "uri2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

