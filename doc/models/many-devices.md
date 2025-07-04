
# Many Devices

*This model accepts additional fields of type Any.*

## Structure

`ManyDevices`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List[DeviceObject]`](../../doc/models/device-object.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "devices": [
    {
      "name": "Kitchen speaker",
      "type": "computer",
      "volume_percent": 59,
      "id": "id4",
      "is_active": false,
      "is_private_session": false,
      "is_restricted": false,
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

