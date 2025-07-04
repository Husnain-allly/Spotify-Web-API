
# Followers Object

*This model accepts additional fields of type Any.*

## Structure

`FollowersObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Optional | This will always be set to null, as the Web API does not support it at the moment. |
| `total` | `int` | Optional | The total number of followers. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "href": "href2",
  "total": 82,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

