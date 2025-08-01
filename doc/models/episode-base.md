
# Episode Base

*This model accepts additional fields of type Any.*

## Structure

`EpisodeBase`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `audio_preview_url` | `str` | Required | A URL to a 30 second preview (MP3 format) of the episode. `null` if not available. |
| `description` | `str` | Required | A description of the episode. HTML tags are stripped away from this field, use `html_description` field in case HTML tags are needed. |
| `html_description` | `str` | Required | A description of the episode. This field may contain HTML tags. |
| `duration_ms` | `int` | Required | The episode length in milliseconds. |
| `explicit` | `bool` | Required | Whether or not the episode has explicit content (true = yes it does; false = no it does not OR unknown). |
| `external_urls` | [`ExternalUrlObject`](../../doc/models/external-url-object.md) | Required | External URLs for this episode. |
| `href` | `str` | Required | A link to the Web API endpoint providing full details of the episode. |
| `id` | `str` | Required | The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the episode. |
| `images` | [`List[ImageObject]`](../../doc/models/image-object.md) | Required | The cover art for the episode in various sizes, widest first. |
| `is_externally_hosted` | `bool` | Required | True if the episode is hosted outside of Spotify's CDN. |
| `is_playable` | `bool` | Required | True if the episode is playable in the given market. Otherwise false. |
| `language` | `str` | Optional | The language used in the episode, identified by a [ISO 639](https://en.wikipedia.org/wiki/ISO_639) code. This field is deprecated and might be removed in the future. Please use the `languages` field instead. |
| `languages` | `List[str]` | Required | A list of the languages used in the episode, identified by their [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639) code. |
| `name` | `str` | Required | The name of the episode. |
| `release_date` | `str` | Required | The date the episode was first released, for example `"1981-12-15"`. Depending on the precision, it might be shown as `"1981"` or `"1981-12"`. |
| `release_date_precision` | [`ReleaseDatePrecision`](../../doc/models/release-date-precision.md) | Required | The precision with which `release_date` value is known. |
| `resume_point` | [`ResumePointObject`](../../doc/models/resume-point-object.md) | Optional | The user's most recent position in the episode. Set if the supplied access token is a user token and has the scope 'user-read-playback-position'. |
| `mtype` | `str` | Required, Constant | The object type.<br><br>**Value**: `'episode'` |
| `uri` | `str` | Required | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the episode. |
| `restrictions` | [`EpisodeRestrictionObject`](../../doc/models/episode-restriction-object.md) | Optional | Included in the response when a content restriction is applied. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "audio_preview_url": "https://p.scdn.co/mp3-preview/2f37da1d4221f40b9d1a98cd191f4d6f1646ad17",
  "description": "A Spotify podcast sharing fresh insights on important topics of the moment—in a way only Spotify can. You’ll hear from experts in the music, podcast and tech industries as we discover and uncover stories about our work and the world around us.\n",
  "html_description": "<p>A Spotify podcast sharing fresh insights on important topics of the moment—in a way only Spotify can. You’ll hear from experts in the music, podcast and tech industries as we discover and uncover stories about our work and the world around us.</p>\n",
  "duration_ms": 1686230,
  "explicit": false,
  "external_urls": {
    "spotify": "spotify6",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "href": "https://api.spotify.com/v1/episodes/5Xt5DXGzch68nYYamXrNxZ",
  "id": "5Xt5DXGzch68nYYamXrNxZ",
  "images": [
    {
      "url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228\n",
      "height": 300,
      "width": 300,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "is_externally_hosted": false,
  "is_playable": false,
  "language": "en",
  "languages": [
    "fr",
    "en"
  ],
  "name": "Starting Your Own Podcast: Tips, Tricks, and Advice From Anchor Creators\n",
  "release_date": "1981-12-15",
  "release_date_precision": "day",
  "type": "episode",
  "uri": "spotify:episode:0zLhl3WsOCQHbe1BPTiHgr",
  "resume_point": {
    "fully_played": false,
    "resume_position_ms": 254,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "restrictions": {
    "reason": "reason0",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

