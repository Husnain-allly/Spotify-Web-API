
# Search Items

*This model accepts additional fields of type Any.*

## Structure

`SearchItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tracks` | [`PagingTrackObject`](../../doc/models/paging-track-object.md) | Optional | - |
| `artists` | [`PagingArtistObject`](../../doc/models/paging-artist-object.md) | Optional | - |
| `albums` | [`PagingSimplifiedAlbumObject`](../../doc/models/paging-simplified-album-object.md) | Optional | - |
| `playlists` | [`PagingPlaylistObject`](../../doc/models/paging-playlist-object.md) | Optional | - |
| `shows` | [`PagingSimplifiedShowObject`](../../doc/models/paging-simplified-show-object.md) | Optional | - |
| `episodes` | [`PagingSimplifiedEpisodeObject`](../../doc/models/paging-simplified-episode-object.md) | Optional | - |
| `audiobooks` | [`PagingSimplifiedAudiobookObject`](../../doc/models/paging-simplified-audiobook-object.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "tracks": {
    "href": "href6",
    "limit": 142,
    "next": "next8",
    "offset": 238,
    "previous": "previous2",
    "total": 236,
    "items": [
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
          }
        ],
        "available_markets": [
          "available_markets2"
        ],
        "disc_number": 244,
        "duration_ms": 52,
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
  "artists": {
    "href": "href2",
    "limit": 214,
    "next": "next2",
    "offset": 54,
    "previous": "previous8",
    "total": 52,
    "items": [
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
          "genres5",
          "genres6"
        ],
        "href": "href0",
        "id": "id8",
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
          "genres5",
          "genres6"
        ],
        "href": "href0",
        "id": "id8",
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
          "genres5",
          "genres6"
        ],
        "href": "href0",
        "id": "id8",
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
  "albums": {
    "href": "href0",
    "limit": 0,
    "next": "next4",
    "offset": 96,
    "previous": "previous6",
    "total": 94,
    "items": [
      {
        "album_type": "album",
        "total_tracks": 196,
        "available_markets": [
          "available_markets2"
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
          },
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
        "release_date_precision": "month",
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
          }
        ],
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
  "playlists": {
    "href": "href2",
    "limit": 68,
    "next": "next2",
    "offset": 164,
    "previous": "previous8",
    "total": 162,
    "items": [
      {
        "collaborative": false,
        "description": "description2",
        "external_urls": {
          "spotify": "spotify6",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        },
        "href": "href0",
        "id": "id8",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      {
        "collaborative": false,
        "description": "description2",
        "external_urls": {
          "spotify": "spotify6",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        },
        "href": "href0",
        "id": "id8",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      {
        "collaborative": false,
        "description": "description2",
        "external_urls": {
          "spotify": "spotify6",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        },
        "href": "href0",
        "id": "id8",
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
  "shows": {
    "href": "href0",
    "limit": 248,
    "next": "next6",
    "offset": 88,
    "previous": "previous6",
    "total": 86,
    "items": [
      {
        "available_markets": [
          "available_markets2"
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
        "description": "description2",
        "html_description": "html_description2",
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
            "url": "url6",
            "height": 182,
            "width": 222,
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          },
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
        "is_externally_hosted": false,
        "languages": [
          "languages5"
        ],
        "media_type": "media_type4",
        "name": "name8",
        "publisher": "publisher4",
        "type": "type2",
        "uri": "uri2",
        "total_episodes": 166,
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      {
        "available_markets": [
          "available_markets2"
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
        "description": "description2",
        "html_description": "html_description2",
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
            "url": "url6",
            "height": 182,
            "width": 222,
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          },
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
        "is_externally_hosted": false,
        "languages": [
          "languages5"
        ],
        "media_type": "media_type4",
        "name": "name8",
        "publisher": "publisher4",
        "type": "type2",
        "uri": "uri2",
        "total_episodes": 166,
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      {
        "available_markets": [
          "available_markets2"
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
        "description": "description2",
        "html_description": "html_description2",
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
            "url": "url6",
            "height": 182,
            "width": 222,
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          },
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
        "is_externally_hosted": false,
        "languages": [
          "languages5"
        ],
        "media_type": "media_type4",
        "name": "name8",
        "publisher": "publisher4",
        "type": "type2",
        "uri": "uri2",
        "total_episodes": 166,
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

