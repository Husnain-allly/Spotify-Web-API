
# Image Object

*This model accepts additional fields of type Any.*

## Structure

`ImageObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Required | The source URL of the image. |
| `height` | `int` | Required | The image height in pixels. |
| `width` | `int` | Required | The image width in pixels. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228\n",
  "height": 300,
  "width": 300,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

