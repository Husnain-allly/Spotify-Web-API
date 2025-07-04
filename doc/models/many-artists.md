
# Many Artists

*This model accepts additional fields of type Any.*

## Structure

`ManyArtists`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `artists` | [`List[ArtistObject]`](../../doc/models/artist-object.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "artists": [
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
      "href": "href2",
      "id": "id0",
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

