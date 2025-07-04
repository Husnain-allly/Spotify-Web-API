
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| environment | `Environment` | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| http_client_instance | `HttpClient` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 30** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| logging_configuration | [`LoggingConfiguration`](../doc/logging-configuration.md) | The SDK logging configuration for API calls |
| client_credentials_auth_credentials | [`ClientCredentialsAuthCredentials`](auth/oauth-2-client-credentials-grant.md) | The credential object for OAuth 2 Client Credentials Grant |

The API client can be initialized as follows:

```python
client = SpotifywebapiClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        oauth_client_id='OAuthClientId',
        oauth_client_secret='OAuthClientSecret',
        oauth_scopes=[
            OauthScope.APP_REMOTE_CONTROL,
            OauthScope.PLAYLIST_READ_PRIVATE
        ]
    ),
    environment=Environment.PRODUCTION,
    logging_configuration=LoggingConfiguration(
        log_level=logging.INFO,
        request_logging_config=RequestLoggingConfiguration(
            log_body=True
        ),
        response_logging_config=ResponseLoggingConfiguration(
            log_headers=True
        )
    )
)
```

## Spotify Web API Client

The gateway for the SDK. This class acts as a factory for the Apis and also holds the configuration of the SDK.

## Apis

| Name | Description |
|  --- | --- |
| albums | Gets AlbumsApi |
| artists | Gets ArtistsApi |
| audiobooks | Gets AudiobooksApi |
| categories | Gets CategoriesApi |
| chapters | Gets ChaptersApi |
| episodes | Gets EpisodesApi |
| genres | Gets GenresApi |
| markets | Gets MarketsApi |
| player | Gets PlayerApi |
| playlists | Gets PlaylistsApi |
| search | Gets SearchApi |
| shows | Gets ShowsApi |
| tracks | Gets TracksApi |
| users | Gets UsersApi |
| oauth_authorization | Gets OauthAuthorizationApi |

