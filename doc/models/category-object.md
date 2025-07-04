
# Category Object

*This model accepts additional fields of type Any.*

## Structure

`CategoryObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Required | A link to the Web API endpoint returning full details of the category. |
| `icons` | [`List[ImageObject]`](../../doc/models/image-object.md) | Required | The category icon, in various sizes. |
| `id` | `str` | Required | The [Spotify category ID](/documentation/web-api/concepts/spotify-uris-ids) of the category. |
| `name` | `str` | Required | The name of the category. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "href": "href0",
  "icons": [
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
  "id": "equal",
  "name": "EQUAL",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

