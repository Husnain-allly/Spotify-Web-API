
# Resume Point Object

*This model accepts additional fields of type Any.*

## Structure

`ResumePointObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fully_played` | `bool` | Optional | Whether or not the episode has been fully played by the user. |
| `resume_position_ms` | `int` | Optional | The user's most recent position in the episode in milliseconds. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "fully_played": false,
  "resume_position_ms": 150,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

