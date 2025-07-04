
# Paged Categories

*This model accepts additional fields of type Any.*

## Structure

`PagedCategories`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `categories` | [`Categories`](../../doc/models/categories.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "categories": {
    "href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20\n",
    "limit": 20,
    "next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
    "offset": 0,
    "previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
    "total": 4,
    "items": [
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

