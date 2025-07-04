
# Playlist Track Object

*This model accepts additional fields of type Any.*

## Structure

`PlaylistTrackObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `added_at` | `datetime` | Optional | The date and time the track or episode was added. _**Note**: some very old playlists may return `null` in this field._ |
| `added_by` | [`PlaylistUserObject`](../../doc/models/playlist-user-object.md) | Optional | The Spotify user who added the track or episode. _**Note**: some very old playlists may return `null` in this field._ |
| `is_local` | `bool` | Optional | Whether this track or episode is a [local file](/documentation/web-api/concepts/playlists/#local-files) or not. |
| `track` | [TrackObject](../../doc/models/track-object.md) \| [EpisodeObject](../../doc/models/episode-object.md) \| None | Optional | This is a container for one-of cases. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "added_at": "2016-03-13T12:52:32.123Z",
  "added_by": {
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
    "href": "href6",
    "id": "id4",
    "type": "user",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "is_local": false,
  "track": {
    "album": {
      "album_type": "single",
      "total_tracks": 170,
      "available_markets": [
        "available_markets2",
        "available_markets3"
      ],
      "external_urls": {
        "spotify": "spotify6",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "href": "href0",
      "id": "id8",
      "images": [
        {
          "url": "url6",
          "height": 182,
          "width": 222,
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        }
      ],
      "name": "name8",
      "release_date": "release_date6",
      "release_date_precision": "day",
      "restrictions": {
        "reason": "explicit",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "type": "type2",
      "uri": "uri2",
      "artists": [
        {
          "external_urls": {
            "spotify": "spotify6",
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          },
          "href": "href2",
          "id": "id0",
          "name": "name0",
          "type": "artist",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        },
        {
          "external_urls": {
            "spotify": "spotify6",
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          },
          "href": "href2",
          "id": "id0",
          "name": "name0",
          "type": "artist",
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
    "artists": [
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
        "genres": [
          "genres7",
          "genres8"
        ],
        "href": "href2",
        "id": "id0",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
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
        "genres": [
          "genres7",
          "genres8"
        ],
        "href": "href2",
        "id": "id0",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      }
    ],
    "available_markets": [
      "available_markets6",
      "available_markets7"
    ],
    "disc_number": 30,
    "duration_ms": 222,
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

