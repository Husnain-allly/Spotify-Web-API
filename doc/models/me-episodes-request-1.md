
# Me Episodes Request 1

*This model accepts additional fields of type Any.*

## Structure

`MeEpisodesRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `List[str]` | Optional | A JSON array of the [Spotify IDs](/documentation/web-api/concepts/spotify-uris-ids). <br/>A maximum of 50 items can be specified in one request. _**Note**: if the `ids` parameter is present in the query string, any IDs listed here in the body will be ignored._ |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "ids": [
    "ids3"
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

