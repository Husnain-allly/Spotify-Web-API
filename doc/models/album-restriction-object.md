
# Album Restriction Object

*This model accepts additional fields of type Any.*

## Structure

`AlbumRestrictionObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | [`Reason`](../../doc/models/reason.md) | Optional | The reason for the restriction. Albums may be restricted if the content is not available in a given market, to the user's subscription type, or when the user's account is set to not play explicit content.<br>Additional reasons may be added in the future. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "reason": "explicit",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

