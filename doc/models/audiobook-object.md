
# Audiobook Object

*This model accepts additional fields of type Any.*

## Structure

`AudiobookObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authors` | [`List[AuthorObject]`](../../doc/models/author-object.md) | Required | The author(s) for the audiobook. |
| `available_markets` | `List[str]` | Required | A list of the countries in which the audiobook can be played, identified by their [ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code. |
| `copyrights` | [`List[CopyrightObject]`](../../doc/models/copyright-object.md) | Required | The copyright statements of the audiobook. |
| `description` | `str` | Required | A description of the audiobook. HTML tags are stripped away from this field, use `html_description` field in case HTML tags are needed. |
| `html_description` | `str` | Required | A description of the audiobook. This field may contain HTML tags. |
| `edition` | `str` | Optional | The edition of the audiobook. |
| `explicit` | `bool` | Required | Whether or not the audiobook has explicit content (true = yes it does; false = no it does not OR unknown). |
| `external_urls` | [`ExternalUrlObject`](../../doc/models/external-url-object.md) | Required | External URLs for this audiobook. |
| `href` | `str` | Required | A link to the Web API endpoint providing full details of the audiobook. |
| `id` | `str` | Required | The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the audiobook. |
| `images` | [`List[ImageObject]`](../../doc/models/image-object.md) | Required | The cover art for the audiobook in various sizes, widest first. |
| `languages` | `List[str]` | Required | A list of the languages used in the audiobook, identified by their [ISO 639](https://en.wikipedia.org/wiki/ISO_639) code. |
| `media_type` | `str` | Required | The media type of the audiobook. |
| `name` | `str` | Required | The name of the audiobook. |
| `narrators` | [`List[NarratorObject]`](../../doc/models/narrator-object.md) | Required | The narrator(s) for the audiobook. |
| `publisher` | `str` | Required | The publisher of the audiobook. |
| `mtype` | `str` | Required, Constant | The object type.<br><br>**Value**: `'audiobook'` |
| `uri` | `str` | Required | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the audiobook. |
| `total_chapters` | `int` | Required | The number of chapters in this audiobook. |
| `chapters` | [`PagingSimplifiedChapterObject`](../../doc/models/paging-simplified-chapter-object.md) | Required | The chapters of the audiobook. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "authors": [
    {
      "name": "name0",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "available_markets": [
    "available_markets2",
    "available_markets3"
  ],
  "copyrights": [
    {
      "text": "text2",
      "type": "type2",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "description": "description8",
  "html_description": "html_description8",
  "edition": "Unabridged",
  "explicit": false,
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
      "url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228\n",
      "height": 300,
      "width": 300,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "languages": [
    "languages5",
    "languages6"
  ],
  "media_type": "media_type6",
  "name": "name8",
  "narrators": [
    {
      "name": "name0",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "publisher": "publisher6",
  "type": "audiobook",
  "uri": "uri2",
  "total_chapters": 236,
  "chapters": {
    "href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20\n",
    "limit": 20,
    "next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
    "offset": 0,
    "previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
    "total": 4,
    "items": [
      {
        "audio_preview_url": "https://p.scdn.co/mp3-preview/2f37da1d4221f40b9d1a98cd191f4d6f1646ad17",
        "chapter_number": 1,
        "description": "We kept on ascending, with occasional periods of quick descent, but in the main always ascending. Suddenly, I became conscious of the fact that the driver was in the act of pulling up the horses in the courtyard of a vast ruined castle, from whose tall black windows came no ray of light, and whose broken battlements showed a jagged line against the moonlit sky.\n",
        "html_description": "<p>We kept on ascending, with occasional periods of quick descent, but in the main always ascending. Suddenly, I became conscious of the fact that the driver was in the act of pulling up the horses in the courtyard of a vast ruined castle, from whose tall black windows came no ray of light, and whose broken battlements showed a jagged line against the moonlit sky.</p>\n",
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
        "is_playable": false,
        "languages": [
          "fr",
          "en"
        ],
        "name": "Starting Your Own Podcast: Tips, Tricks, and Advice From Anchor Creators\n",
        "release_date": "1981-12-15",
        "release_date_precision": "day",
        "type": "episode",
        "uri": "spotify:episode:0zLhl3WsOCQHbe1BPTiHgr",
        "available_markets": [
          "available_markets2"
        ],
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
    ],
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

