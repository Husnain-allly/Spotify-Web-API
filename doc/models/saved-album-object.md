
# Saved Album Object

*This model accepts additional fields of type Any.*

## Structure

`SavedAlbumObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `added_at` | `datetime` | Optional | The date and time the album was saved<br>Timestamps are returned in ISO 8601 format as Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ.<br>If the time is imprecise (for example, the date/time of an album release), an additional field indicates the precision; see for example, release_date in an album object. |
| `album` | [`AlbumObject`](../../doc/models/album-object.md) | Optional | Information about the album. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "added_at": "2016-03-13T12:52:32.123Z",
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
    "tracks": {
      "href": "href6",
      "limit": 142,
      "next": "next8",
      "offset": 238,
      "previous": "previous2",
      "total": 236,
      "items": [
        {
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
            }
          ],
          "available_markets": [
            "available_markets2"
          ],
          "disc_number": 244,
          "duration_ms": 52,
          "explicit": false,
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
    "copyrights": [
      {
        "text": "text2",
        "type": "type2",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      {
        "text": "text2",
        "type": "type2",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      }
    ],
    "external_ids": {
      "isrc": "isrc8",
      "ean": "ean8",
      "upc": "upc2",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "genres": [
      "genres5",
      "genres6",
      "genres7"
    ],
    "label": "label8",
    "popularity": 78,
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

