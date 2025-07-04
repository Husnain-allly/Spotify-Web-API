
# Cursor Paging Simplified Artist Object

*This model accepts additional fields of type Any.*

## Structure

`CursorPagingSimplifiedArtistObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Optional | A link to the Web API endpoint returning the full result of the request. |
| `limit` | `int` | Optional | The maximum number of items in the response (as set in the query or by default). |
| `next` | `str` | Optional | URL to the next page of items. ( `null` if none) |
| `cursors` | [`CursorObject`](../../doc/models/cursor-object.md) | Optional | The cursors used to find the next set of items. |
| `total` | `int` | Optional | The total number of items available to return. |
| `items` | [`List[ArtistObject]`](../../doc/models/artist-object.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "href": "href2",
  "limit": 160,
  "next": "next8",
  "cursors": {
    "after": "after8",
    "before": "before6",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "total": 254,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

