
# Audio Analysis Object

*This model accepts additional fields of type Any.*

## Structure

`AudioAnalysisObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `meta` | [`Meta`](../../doc/models/meta.md) | Optional | - |
| `track` | [`Track`](../../doc/models/track.md) | Optional | - |
| `bars` | [`List[TimeIntervalObject]`](../../doc/models/time-interval-object.md) | Optional | The time intervals of the bars throughout the track. A bar (or measure) is a segment of time defined as a given number of beats. |
| `beats` | [`List[TimeIntervalObject]`](../../doc/models/time-interval-object.md) | Optional | The time intervals of beats throughout the track. A beat is the basic time unit of a piece of music; for example, each tick of a metronome. Beats are typically multiples of tatums. |
| `sections` | [`List[SectionObject]`](../../doc/models/section-object.md) | Optional | Sections are defined by large variations in rhythm or timbre, e.g. chorus, verse, bridge, guitar solo, etc. Each section contains its own descriptions of tempo, key, mode, time_signature, and loudness. |
| `segments` | [`List[SegmentObject]`](../../doc/models/segment-object.md) | Optional | Each segment contains a roughly conisistent sound throughout its duration. |
| `tatums` | [`List[TimeIntervalObject]`](../../doc/models/time-interval-object.md) | Optional | A tatum represents the lowest regular pulse train that a listener intuitively infers from the timing of perceived musical events (segments). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "meta": {
    "analyzer_version": "analyzer_version8",
    "platform": "platform6",
    "detailed_status": "detailed_status8",
    "status_code": 168,
    "timestamp": 220,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "track": {
    "num_samples": 156,
    "duration": 53.8,
    "sample_md5": "sample_md56",
    "offset_seconds": 172,
    "window_seconds": 42,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "bars": [
    {
      "start": 141.7,
      "duration": 145.82,
      "confidence": 1.0,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "beats": [
    {
      "start": 102.56,
      "duration": 106.68,
      "confidence": 1.0,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "sections": [
    {
      "start": 112.18,
      "duration": 116.3,
      "confidence": 1.0,
      "loudness": 14.46,
      "tempo": 25.0,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "start": 112.18,
      "duration": 116.3,
      "confidence": 1.0,
      "loudness": 14.46,
      "tempo": 25.0,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "start": 112.18,
      "duration": 116.3,
      "confidence": 1.0,
      "loudness": 14.46,
      "tempo": 25.0,
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

