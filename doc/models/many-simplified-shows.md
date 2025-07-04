
# Many Simplified Shows

*This model accepts additional fields of type Any.*

## Structure

`ManySimplifiedShows`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `shows` | [`List[ShowBase]`](../../doc/models/show-base.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "shows": [
    {
      "available_markets": [
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
        }
      ],
      "description": "description8",
      "html_description": "html_description2",
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
          "url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228\n",
          "height": 300,
          "width": 300,
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        }
      ],
      "is_externally_hosted": false,
      "languages": [
        "languages5"
      ],
      "media_type": "media_type4",
      "name": "name8",
      "publisher": "publisher4",
      "type": "show",
      "uri": "uri2",
      "total_episodes": 196,
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

