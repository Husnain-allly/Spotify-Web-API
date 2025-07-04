
# Me Following Request

*This model accepts additional fields of type Any.*

## Structure

`MeFollowingRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `List[str]` | Required | A JSON array of the artist or user [Spotify IDs](/documentation/web-api/concepts/spotify-uris-ids).<br>For example: `{ids:["74ASZWbe4lXaubB36ztrGX", "08td7MxkoHQkXnWAYD8d6Q"]}`. A maximum of 50 IDs can be sent in one request. _**Note**: if the `ids` parameter is present in the query string, any IDs listed here in the body will be ignored._ |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "ids": [
    "ids5",
    "ids6"
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

