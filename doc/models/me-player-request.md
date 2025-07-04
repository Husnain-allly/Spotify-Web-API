
# Me Player Request

*This model accepts additional fields of type Any.*

## Structure

`MePlayerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | `List[str]` | Required | A JSON array containing the ID of the device on which playback should be started/transferred.<br/>For example:`{device_ids:["74ASZWbe4lXaubB36ztrGX"]}`<br/>_**Note**: Although an array is accepted, only a single device_id is currently supported. Supplying more than one will return `400 Bad Request`_ |
| `play` | `bool` | Optional | **true**: ensure playback happens on new device.<br/>**false** or not provided: keep the current playback state. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "device_ids": [
    "74ASZWbe4lXaubB36ztrGX"
  ],
  "play": false,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

