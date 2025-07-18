
# Saved Show Object

*This model accepts additional fields of type Any.*

## Structure

`SavedShowObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `added_at` | `datetime` | Optional | The date and time the show was saved.<br>Timestamps are returned in ISO 8601 format as Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ.<br>If the time is imprecise (for example, the date/time of an album release), an additional field indicates the precision; see for example, release_date in an album object. |
| `show` | [`ShowBase`](../../doc/models/show-base.md) | Optional | Information about the show. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "added_at": "2016-03-13T12:52:32.123Z",
  "show": {
    "available_markets": [
      "available_markets0",
      "available_markets1",
      "available_markets2"
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
    "description": "description4",
    "html_description": "html_description4",
    "explicit": false,
    "external_urls": {
      "spotify": "spotify6",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "href": "href8",
    "id": "id6",
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
    "is_externally_hosted": false,
    "languages": [
      "languages7",
      "languages6",
      "languages5"
    ],
    "media_type": "media_type6",
    "name": "name6",
    "publisher": "publisher6",
    "type": "type4",
    "uri": "uri0",
    "total_episodes": 198,
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

