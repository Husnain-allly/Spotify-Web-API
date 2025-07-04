
# Many Tracks

*This model accepts additional fields of type Any.*

## Structure

`ManyTracks`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tracks` | [`List[TrackObject]`](../../doc/models/track-object.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "tracks": [
    {
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
        "available_markets8",
        "available_markets9"
      ],
      "disc_number": 168,
      "duration_ms": 232,
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
}
```

