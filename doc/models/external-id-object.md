
# External Id Object

*This model accepts additional fields of type Any.*

## Structure

`ExternalIdObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `isrc` | `str` | Optional | [International Standard Recording Code](http://en.wikipedia.org/wiki/International_Standard_Recording_Code) |
| `ean` | `str` | Optional | [International Article Number](http://en.wikipedia.org/wiki/International_Article_Number_%28EAN%29) |
| `upc` | `str` | Optional | [Universal Product Code](http://en.wikipedia.org/wiki/Universal_Product_Code) |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "isrc": "isrc2",
  "ean": "ean4",
  "upc": "upc8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

