
# Getting Started with Spotify Web API

## Introduction

You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.

In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href="https://developer.spotify.com/documentation/general/guides/authorization-guide/">OAuth 2.0</a>.

The base URI for all Web API requests is `https://api.spotify.com/v1`.

Need help? See our <a href="https://developer.spotify.com/documentation/web-api/guides/">Web API guides</a> for more information, or visit the <a href="https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer">Spotify for Developers community forum</a> to ask questions and connect with other developers.

## Building

You must have Python `3.7+` installed on your system to install and run this SDK. This SDK package depends on other Python packages like pytest, etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK. To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Spotifywebapi-Python&step=installDependencies)

## Installation

The following section explains how to use the spotifywebapi library in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Spotifywebapi-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Spotifywebapi-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Spotifywebapi-Python&projectName=spotifywebapi&step=openProject1)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Spotifywebapi-Python&projectName=spotifywebapi&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Spotifywebapi-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Spotifywebapi-Python&projectName=spotifywebapi&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Spotifywebapi-Python&projectName=spotifywebapi&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from spotifywebapi.spotifywebapi_client import SpotifywebapiClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Spotifywebapi-Python&projectName=spotifywebapi&libraryName=spotifywebapi.spotifywebapi_client&className=SpotifywebapiClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Spotifywebapi-Python&projectName=spotifywebapi&libraryName=spotifywebapi.spotifywebapi_client&className=SpotifywebapiClient&step=runProject)

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](doc/client.md)

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
| logging_configuration | [`LoggingConfiguration`](doc/logging-configuration.md) | The SDK logging configuration for API calls |
| client_credentials_auth_credentials | [`ClientCredentialsAuthCredentials`](doc/auth/oauth-2-client-credentials-grant.md) | The credential object for OAuth 2 Client Credentials Grant |

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

## Authorization

This API uses the following authentication schemes.

* [`oauth_2_0 (OAuth 2 Client Credentials Grant)`](doc/auth/oauth-2-client-credentials-grant.md)

## List of APIs

* [Albums](doc/controllers/albums.md)
* [Artists](doc/controllers/artists.md)
* [Audiobooks](doc/controllers/audiobooks.md)
* [Categories](doc/controllers/categories.md)
* [Chapters](doc/controllers/chapters.md)
* [Episodes](doc/controllers/episodes.md)
* [Genres](doc/controllers/genres.md)
* [Markets](doc/controllers/markets.md)
* [Player](doc/controllers/player.md)
* [Playlists](doc/controllers/playlists.md)
* [Search](doc/controllers/search.md)
* [Shows](doc/controllers/shows.md)
* [Tracks](doc/controllers/tracks.md)
* [Users](doc/controllers/users.md)

## SDK Infrastructure

### Configuration

* [AbstractLogger](doc/abstract-logger.md)
* [LoggingConfiguration](doc/logging-configuration.md)
* [RequestLoggingConfiguration](doc/request-logging-configuration.md)
* [ResponseLoggingConfiguration](doc/response-logging-configuration.md)

### HTTP

* [HttpResponse](doc/http-response.md)
* [HttpRequest](doc/http-request.md)

### Utilities

* [ApiResponse](doc/api-response.md)
* [ApiHelper](doc/api-helper.md)
* [HttpDateTime](doc/http-date-time.md)
* [RFC3339DateTime](doc/rfc3339-date-time.md)
* [UnixDateTime](doc/unix-date-time.md)

