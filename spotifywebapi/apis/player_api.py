# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from spotifywebapi.api_helper import APIHelper
from spotifywebapi.configuration import Server
from spotifywebapi.http.api_response import ApiResponse
from spotifywebapi.apis.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from spotifywebapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from spotifywebapi.models.currently_playing_context_object import CurrentlyPlayingContextObject
from spotifywebapi.models.many_devices import ManyDevices
from spotifywebapi.models.currently_playing_object import CurrentlyPlayingObject
from spotifywebapi.models.cursor_paging_play_history_object import CursorPagingPlayHistoryObject
from spotifywebapi.models.queue_object import QueueObject
from spotifywebapi.exceptions.unauthorized_exception import UnauthorizedException
from spotifywebapi.exceptions.forbidden_exception import ForbiddenException
from spotifywebapi.exceptions.too_many_requests_exception import TooManyRequestsException


class PlayerApi(BaseApi):

    """A Controller to access Endpoints in the spotifywebapi API."""
    def __init__(self, config):
        super(PlayerApi, self).__init__(config)

    def get_information_about_the_users_current_playback(self,
                                                         market=None,
                                                         additional_types=None):
        """Does a GET request to /me/player.

        Get information about the user’s current playback state, including
        track or episode, progress, and active device.

        Args:
            market (str, optional): The request query parameter.
            additional_types (str, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.
                Information about playback

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/player')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('market')
                         .value(market))
            .query_param(Parameter()
                         .key('additional_types')
                         .value(additional_types))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CurrentlyPlayingContextObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def transfer_a_users_playback(self,
                                  body=None):
        """Does a PUT request to /me/player.

        Transfer playback to a new device and optionally begin playback. This
        API only works for users who have Spotify Premium. The order of
        execution is not guaranteed when you use this API with other Player
        API endpoints.

        Args:
            body (MePlayerRequest, optional): The request body parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Playback
                transferred

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/player')
            .http_method(HttpMethodEnum.PUT)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_a_users_available_devices(self):
        """Does a GET request to /me/player/devices.

        Get information about a user’s available Spotify Connect devices. Some
        device models are not supported and will not be listed in the API
        response.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A set of
                devices

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/player/devices')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ManyDevices.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_the_users_currently_playing_track(self,
                                              market=None,
                                              additional_types=None):
        """Does a GET request to /me/player/currently-playing.

        Get the object currently being played on the user's Spotify account.

        Args:
            market (str, optional): The request query parameter.
            additional_types (str, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.
                Information about the currently playing track

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/player/currently-playing')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('market')
                         .value(market))
            .query_param(Parameter()
                         .key('additional_types')
                         .value(additional_types))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CurrentlyPlayingObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def start_a_users_playback(self,
                               device_id=None,
                               body=None):
        """Does a PUT request to /me/player/play.

        Start a new context or resume current playback on the user's active
        device. This API only works for users who have Spotify Premium. The
        order of execution is not guaranteed when you use this API with other
        Player API endpoints.

        Args:
            device_id (str, optional): The request query parameter.
            body (MePlayerPlayRequest, optional): The request body parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Playback
                started

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/player/play')
            .http_method(HttpMethodEnum.PUT)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .query_param(Parameter()
                         .key('device_id')
                         .value(device_id))
            .body_param(Parameter()
                        .value(body))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def pause_a_users_playback(self,
                               device_id=None):
        """Does a PUT request to /me/player/pause.

        Pause playback on the user's account. This API only works for users
        who have Spotify Premium. The order of execution is not guaranteed
        when you use this API with other Player API endpoints.

        Args:
            device_id (str, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Playback
                paused

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/player/pause')
            .http_method(HttpMethodEnum.PUT)
            .query_param(Parameter()
                         .key('device_id')
                         .value(device_id))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def skip_users_playback_to_next_track(self,
                                          device_id=None):
        """Does a POST request to /me/player/next.

        Skips to next track in the user’s queue. This API only works for users
        who have Spotify Premium. The order of execution is not guaranteed
        when you use this API with other Player API endpoints.

        Args:
            device_id (str, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Command
                sent

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/player/next')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('device_id')
                         .value(device_id))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def skip_users_playback_to_previous_track(self,
                                              device_id=None):
        """Does a POST request to /me/player/previous.

        Skips to previous track in the user’s queue. This API only works for
        users who have Spotify Premium. The order of execution is not
        guaranteed when you use this API with other Player API endpoints.

        Args:
            device_id (str, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Command
                sent

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/player/previous')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('device_id')
                         .value(device_id))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def seek_to_position_in_currently_playing_track(self,
                                                    position_ms,
                                                    device_id=None):
        """Does a PUT request to /me/player/seek.

        Seeks to the given position in the user’s currently playing track.
        This API only works for users who have Spotify Premium. The order of
        execution is not guaranteed when you use this API with other Player
        API endpoints.

        Args:
            position_ms (int): The request query parameter.
            device_id (str, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Command
                sent

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/player/seek')
            .http_method(HttpMethodEnum.PUT)
            .query_param(Parameter()
                         .key('position_ms')
                         .value(position_ms)
                         .is_required(True))
            .query_param(Parameter()
                         .key('device_id')
                         .value(device_id))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def set_repeat_mode_on_users_playback(self,
                                          state,
                                          device_id=None):
        """Does a PUT request to /me/player/repeat.

        Set the repeat mode for the user's playback. This API only works for
        users who have Spotify Premium. The order of execution is not
        guaranteed when you use this API with other Player API endpoints.

        Args:
            state (str): The request query parameter.
            device_id (str, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Command
                sent

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/player/repeat')
            .http_method(HttpMethodEnum.PUT)
            .query_param(Parameter()
                         .key('state')
                         .value(state)
                         .is_required(True))
            .query_param(Parameter()
                         .key('device_id')
                         .value(device_id))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def set_volume_for_users_playback(self,
                                      volume_percent,
                                      device_id=None):
        """Does a PUT request to /me/player/volume.

        Set the volume for the user’s current playback device. This API only
        works for users who have Spotify Premium. The order of execution is
        not guaranteed when you use this API with other Player API endpoints.

        Args:
            volume_percent (int): The request query parameter.
            device_id (str, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Command
                sent

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/player/volume')
            .http_method(HttpMethodEnum.PUT)
            .query_param(Parameter()
                         .key('volume_percent')
                         .value(volume_percent)
                         .is_required(True))
            .query_param(Parameter()
                         .key('device_id')
                         .value(device_id))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def toggle_shuffle_for_users_playback(self,
                                          state,
                                          device_id=None):
        """Does a PUT request to /me/player/shuffle.

        Toggle shuffle on or off for user’s playback. This API only works for
        users who have Spotify Premium. The order of execution is not
        guaranteed when you use this API with other Player API endpoints.

        Args:
            state (bool): The request query parameter.
            device_id (str, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Command
                sent

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/player/shuffle')
            .http_method(HttpMethodEnum.PUT)
            .query_param(Parameter()
                         .key('state')
                         .value(state)
                         .is_required(True))
            .query_param(Parameter()
                         .key('device_id')
                         .value(device_id))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_recently_played(self,
                            limit=20,
                            after=None,
                            before=None):
        """Does a GET request to /me/player/recently-played.

        Get tracks from the current user's recently played tracks.
        _**Note**: Currently doesn't support podcast episodes._

        Args:
            limit (int, optional): The request query parameter. Example: 20
            after (int, optional): The request query parameter.
            before (int, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A paged
                set of tracks

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/player/recently-played')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('after')
                         .value(after))
            .query_param(Parameter()
                         .key('before')
                         .value(before))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CursorPagingPlayHistoryObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_queue(self):
        """Does a GET request to /me/player/queue.

        Get the list of objects that make up the user's queue.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.
                Information about the queue

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/player/queue')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(QueueObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def add_to_queue(self,
                     uri,
                     device_id=None):
        """Does a POST request to /me/player/queue.

        Add an item to the end of the user's current playback queue. This API
        only works for users who have Spotify Premium. The order of execution
        is not guaranteed when you use this API with other Player API
        endpoints.

        Args:
            uri (str): The request query parameter.
            device_id (str, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Command
                received

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/player/queue')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('uri')
                         .value(uri)
                         .is_required(True))
            .query_param(Parameter()
                         .key('device_id')
                         .value(device_id))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()
