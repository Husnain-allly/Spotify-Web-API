
# Paging Featured Playlist Object

*This model accepts additional fields of type Any.*

## Structure

`PagingFeaturedPlaylistObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Optional | The localized message of a playlist. |
| `playlists` | [`PagingPlaylistObject`](../../doc/models/paging-playlist-object.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "message": "Popular Playlists",
  "playlists": {
    "href": "href2",
    "limit": 68,
    "next": "next2",
    "offset": 164,
    "previous": "previous8",
    "total": 162,
    "items": [
      {
        "collaborative": false,
        "description": "description2",
        "external_urls": {
          "spotify": "spotify6",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        },
        "href": "href0",
        "id": "id8",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      {
        "collaborative": false,
        "description": "description2",
        "external_urls": {
          "spotify": "spotify6",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        },
        "href": "href0",
        "id": "id8",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      {
        "collaborative": false,
        "description": "description2",
        "external_urls": {
          "spotify": "spotify6",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        },
        "href": "href0",
        "id": "id8",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      }
    ],
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

