
# Playlists Tracks Request 2

*This model accepts additional fields of type Any.*

## Structure

`PlaylistsTracksRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tracks` | [`List[Track1]`](../../doc/models/track-1.md) | Required | An array of objects containing [Spotify URIs](/documentation/web-api/concepts/spotify-uris-ids) of the tracks or episodes to remove.<br>For example: `{ "tracks": [{ "uri": "spotify:track:4iV5W9uYEdYUVa79Axb7Rh" },{ "uri": "spotify:track:1301WleyT98MSxVHPZCA6M" }] }`. A maximum of 100 objects can be sent at once. |
| `snapshot_id` | `str` | Optional | The playlist's snapshot ID against which you want to make the changes.<br>The API will validate that the specified items exist and in the specified positions and make the changes,<br>even if more recent changes have been made to the playlist. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "tracks": [
    {
      "uri": "uri8",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "snapshot_id": "snapshot_id8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

