
# Track Object

*This model accepts additional fields of type Any.*

## Structure

`TrackObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `album` | [`SimplifiedAlbumObject`](../../doc/models/simplified-album-object.md) | Optional | The album on which the track appears. The album object includes a link in `href` to full information about the album. |
| `artists` | [`List[ArtistObject]`](../../doc/models/artist-object.md) | Optional | The artists who performed the track. Each artist object includes a link in `href` to more detailed information about the artist. |
| `available_markets` | `List[str]` | Optional | A list of the countries in which the track can be played, identified by their [ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. |
| `disc_number` | `int` | Optional | The disc number (usually `1` unless the album consists of more than one disc). |
| `duration_ms` | `int` | Optional | The track length in milliseconds. |
| `explicit` | `bool` | Optional | Whether or not the track has explicit lyrics ( `true` = yes it does; `false` = no it does not OR unknown). |
| `external_ids` | [`ExternalIdObject`](../../doc/models/external-id-object.md) | Optional | Known external IDs for the track. |
| `external_urls` | [`ExternalUrlObject`](../../doc/models/external-url-object.md) | Optional | Known external URLs for this track. |
| `href` | `str` | Optional | A link to the Web API endpoint providing full details of the track. |
| `id` | `str` | Optional | The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the track. |
| `is_playable` | `bool` | Optional | Part of the response when [Track Relinking](/documentation/web-api/concepts/track-relinking) is applied. If `true`, the track is playable in the given market. Otherwise `false`. |
| `linked_from` | [`LinkedTrackObject`](../../doc/models/linked-track-object.md) | Optional | Part of the response when [Track Relinking](/documentation/web-api/concepts/track-relinking) is applied, and the requested track has been replaced with different track. The track in the `linked_from` object contains information about the originally requested track. |
| `restrictions` | [`TrackRestrictionObject`](../../doc/models/track-restriction-object.md) | Optional | Included in the response when a content restriction is applied. |
| `name` | `str` | Optional | The name of the track. |
| `popularity` | `int` | Optional | The popularity of the track. The value will be between 0 and 100, with 100 being the most popular.<br/>The popularity of a track is a value between 0 and 100, with 100 being the most popular. The popularity is calculated by algorithm and is based, in the most part, on the total number of plays the track has had and how recent those plays are.<br/>Generally speaking, songs that are being played a lot now will have a higher popularity than songs that were played a lot in the past. Duplicate tracks (e.g. the same track from a single and an album) are rated independently. Artist and album popularity is derived mathematically from track popularity. _**Note**: the popularity value may lag actual popularity by a few days: the value is not updated in real time._ |
| `preview_url` | `str` | Optional | A link to a 30 second preview (MP3 format) of the track. Can be `null` |
| `track_number` | `int` | Optional | The number of the track. If an album has several discs, the track number is the number on the specified disc. |
| `mtype` | [`Type2`](../../doc/models/type-2.md) | Optional | The object type: "track". |
| `uri` | `str` | Optional | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the track. |
| `is_local` | `bool` | Optional | Whether or not the track is from a local file. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "album": {
    "album_type": "single",
    "total_tracks": 170,
    "available_markets": [
      "available_markets2",
      "available_markets3"
    ],
    "external_urls": {
      "spotify": "spotify6",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "href": "href0",
    "id": "id8",
    "images": [
      {
        "url": "url6",
        "height": 182,
        "width": 222,
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      }
    ],
    "name": "name8",
    "release_date": "release_date6",
    "release_date_precision": "day",
    "restrictions": {
      "reason": "explicit",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "type": "type2",
    "uri": "uri2",
    "artists": [
      {
        "external_urls": {
          "spotify": "spotify6",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        },
        "href": "href2",
        "id": "id0",
        "name": "name0",
        "type": "artist",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      {
        "external_urls": {
          "spotify": "spotify6",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        },
        "href": "href2",
        "id": "id0",
        "name": "name0",
        "type": "artist",
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
  },
  "artists": [
    {
      "external_urls": {
        "spotify": "spotify6",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "followers": {
        "href": "href0",
        "total": 82,
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "genres": [
        "genres7",
        "genres8"
      ],
      "href": "href2",
      "id": "id0",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "external_urls": {
        "spotify": "spotify6",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "followers": {
        "href": "href0",
        "total": 82,
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "genres": [
        "genres7",
        "genres8"
      ],
      "href": "href2",
      "id": "id0",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "available_markets": [
    "available_markets6",
    "available_markets7"
  ],
  "disc_number": 30,
  "duration_ms": 222,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

