
# Disallows Object

*This model accepts additional fields of type Any.*

## Structure

`DisallowsObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `interrupting_playback` | `bool` | Optional | Interrupting playback. Optional field. |
| `pausing` | `bool` | Optional | Pausing. Optional field. |
| `resuming` | `bool` | Optional | Resuming. Optional field. |
| `seeking` | `bool` | Optional | Seeking playback location. Optional field. |
| `skipping_next` | `bool` | Optional | Skipping to the next context. Optional field. |
| `skipping_prev` | `bool` | Optional | Skipping to the previous context. Optional field. |
| `toggling_repeat_context` | `bool` | Optional | Toggling repeat context flag. Optional field. |
| `toggling_shuffle` | `bool` | Optional | Toggling shuffle flag. Optional field. |
| `toggling_repeat_track` | `bool` | Optional | Toggling repeat track flag. Optional field. |
| `transferring_playback` | `bool` | Optional | Transfering playback between devices. Optional field. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "interrupting_playback": false,
  "pausing": false,
  "resuming": false,
  "seeking": false,
  "skipping_next": false,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

