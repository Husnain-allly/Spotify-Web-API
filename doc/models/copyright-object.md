
# Copyright Object

*This model accepts additional fields of type Any.*

## Structure

`CopyrightObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Optional | The copyright text for this content. |
| `mtype` | `str` | Optional | The type of copyright: `C` = the copyright, `P` = the sound recording (performance) copyright. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "text": "text8",
  "type": "type2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

