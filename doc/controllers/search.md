# Search

```python
search_api = client.search
```

## Class Name

`SearchApi`


# Search

Get Spotify catalog information about albums, artists, playlists, tracks, shows, episodes or audiobooks
that match a keyword string. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.

```python
def search(self,
          q,
          mtype,
          market=None,
          limit=20,
          offset=0,
          include_external=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `q` | `str` | Query, Required | - |
| `mtype` | [`List[ItemType]`](../../doc/models/item-type.md) | Query, Required | - |
| `market` | `str` | Query, Optional | - |
| `limit` | `int` | Query, Optional | **Default**: `20`<br><br>**Constraints**: `>= 1`, `<= 50` |
| `offset` | `int` | Query, Optional | **Default**: `0`<br><br>**Constraints**: `>= 0`, `<= 1000` |
| `include_external` | [`IncludeExternal`](../../doc/models/include-external.md) | Query, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SearchItems`](../../doc/models/search-items.md).

## Example Usage

```python
q = 'remaster%20track:Doxy%20artist:Miles%20Davis'

mtype = [
    ItemType.AUDIOBOOK,
    ItemType.ALBUM,
    ItemType.ARTIST
]

market = 'ES'

limit = 10

offset = 5

result = search_api.search(
    q,
    mtype,
    market=market,
    limit=limit,
    offset=offset
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |

