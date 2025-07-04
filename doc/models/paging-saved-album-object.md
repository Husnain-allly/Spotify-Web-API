
# Paging Saved Album Object

*This model accepts additional fields of type Any.*

## Structure

`PagingSavedAlbumObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Required | A link to the Web API endpoint returning the full result of the request |
| `limit` | `int` | Required | The maximum number of items in the response (as set in the query or by default). |
| `next` | `str` | Required | URL to the next page of items. ( `null` if none) |
| `offset` | `int` | Required | The offset of the items returned (as set in the query or by default) |
| `previous` | `str` | Required | URL to the previous page of items. ( `null` if none) |
| `total` | `int` | Required | The total number of items available to return. |
| `items` | [`List[SavedAlbumObject]`](../../doc/models/saved-album-object.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20\n",
  "limit": 20,
  "next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
  "offset": 0,
  "previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
  "total": 4,
  "items": [
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
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

