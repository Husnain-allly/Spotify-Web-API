
# Paging Artist Object

*This model accepts additional fields of type Any.*

## Structure

`PagingArtistObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Required | A link to the Web API endpoint returning the full result of the request |
| `limit` | `int` | Required | The maximum number of items in the response (as set in the query or by default). |
| `next` | `str` | Required | URL to the next page of items. ( `null` if none) |
| `offset` | `int` | Required | The offset of the items returned (as set in the query or by default) |
| `previous` | `str` | Required | URL to the previous page of items. ( `null` if none) |
| `total` | `int` | Required | The total number of items available to return. |
| `items` | [`List[ArtistObject]`](../../doc/models/artist-object.md) | Required | - |
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
      "genres": [
        "Prog rock",
        "Grunge"
      ],
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
}
```

