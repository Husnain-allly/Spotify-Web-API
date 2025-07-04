
# Cursor Paged Artists

*This model accepts additional fields of type Any.*

## Structure

`CursorPagedArtists`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `artists` | [`CursorPagingSimplifiedArtistObject`](../../doc/models/cursor-paging-simplified-artist-object.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "artists": {
    "href": "href2",
    "limit": 214,
    "next": "next2",
    "cursors": {
      "after": "after8",
      "before": "before6",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "total": 52,
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

