
# Paging Saved Audiobook Object

*This model accepts additional fields of type Any.*

## Structure

`PagingSavedAudiobookObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Required | A link to the Web API endpoint returning the full result of the request |
| `limit` | `int` | Required | The maximum number of items in the response (as set in the query or by default). |
| `next` | `str` | Required | URL to the next page of items. ( `null` if none) |
| `offset` | `int` | Required | The offset of the items returned (as set in the query or by default) |
| `previous` | `str` | Required | URL to the previous page of items. ( `null` if none) |
| `total` | `int` | Required | The total number of items available to return. |
| `items` | [`List[SavedAudiobookObject]`](../../doc/models/saved-audiobook-object.md) | Required | - |
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
      "audiobook": {
        "authors": [
          {
            "name": "name0",
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          }
        ],
        "available_markets": [
          "available_markets2",
          "available_markets3",
          "available_markets4"
        ],
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
        "description": "description2",
        "html_description": "html_description2",
        "edition": "edition8",
        "explicit": false,
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
          },
          {
            "url": "url6",
            "height": 182,
            "width": 222,
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          },
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
        "languages": [
          "languages3",
          "languages4"
        ],
        "media_type": "media_type4",
        "name": "name8",
        "narrators": [
          {
            "name": "name0",
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          },
          {
            "name": "name0",
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          }
        ],
        "publisher": "publisher4",
        "type": "type2",
        "uri": "uri2",
        "total_chapters": 186,
        "chapters": {
          "href": "href4",
          "limit": 230,
          "next": "next0",
          "offset": 122,
          "previous": "previous0",
          "total": 136,
          "items": [
            {
              "audio_preview_url": "audio_preview_url4",
              "available_markets": [
                "available_markets2"
              ],
              "chapter_number": 164,
              "description": "description2",
              "html_description": "html_description2",
              "duration_ms": 52,
              "explicit": false,
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
                },
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
              "is_playable": false,
              "languages": [
                "languages5"
              ],
              "name": "name8",
              "release_date": "release_date6",
              "release_date_precision": "month",
              "resume_point": {
                "fully_played": false,
                "resume_position_ms": 254,
                "exampleAdditionalProperty": {
                  "key1": "val1",
                  "key2": "val2"
                }
              },
              "type": "type2",
              "uri": "uri2",
              "restrictions": {
                "reason": "reason0",
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
        },
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

