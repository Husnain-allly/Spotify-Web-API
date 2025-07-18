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
from spotifywebapi.models.private_user_object import PrivateUserObject
from spotifywebapi.models.public_user_object import PublicUserObject
from spotifywebapi.models.cursor_paged_artists import CursorPagedArtists
from spotifywebapi.models.paging_artist_object import PagingArtistObject
from spotifywebapi.models.paging_track_object import PagingTrackObject
from spotifywebapi.exceptions.unauthorized_exception import UnauthorizedException
from spotifywebapi.exceptions.forbidden_exception import ForbiddenException
from spotifywebapi.exceptions.too_many_requests_exception import TooManyRequestsException


class UsersApi(BaseApi):

    """A Controller to access Endpoints in the spotifywebapi API."""
    def __init__(self, config):
        super(UsersApi, self).__init__(config)

    def get_current_users_profile(self):
        """Does a GET request to /me.

        Get detailed profile information about the current user (including the
        current user's username).

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A user

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PrivateUserObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_users_profile(self,
                          user_id):
        """Does a GET request to /users/{user_id}.

        Get public profile information about a Spotify user.

        Args:
            user_id (str): The request template parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A user

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/users/{user_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('user_id')
                            .value(user_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PublicUserObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def follow_playlist(self,
                        playlist_id,
                        body=None):
        """Does a PUT request to /playlists/{playlist_id}/followers.

        Add the current user as a follower of a playlist.

        Args:
            playlist_id (str): The request template parameter.
            body (PlaylistsFollowersRequest, optional): The request body
                parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Playlist
                followed

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/playlists/{playlist_id}/followers')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('playlist_id')
                            .value(playlist_id)
                            .is_required(True)
                            .should_encode(True))
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

    def unfollow_playlist(self,
                          playlist_id):
        """Does a DELETE request to /playlists/{playlist_id}/followers.

        Remove the current user as a follower of a playlist.

        Args:
            playlist_id (str): The request template parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Playlist
                unfollowed

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/playlists/{playlist_id}/followers')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('playlist_id')
                            .value(playlist_id)
                            .is_required(True)
                            .should_encode(True))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_followed(self,
                     mtype,
                     after=None,
                     limit=20):
        """Does a GET request to /me/following.

        Get the current user's followed artists.

        Args:
            mtype (ItemType1): The request query parameter.
            after (str, optional): The request query parameter.
            limit (int, optional): The request query parameter. Example: 20

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A paged
                set of artists

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/following')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('type')
                         .value(mtype)
                         .is_required(True))
            .query_param(Parameter()
                         .key('after')
                         .value(after))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CursorPagedArtists.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def follow_artists_users(self,
                             mtype,
                             ids,
                             body=None):
        """Does a PUT request to /me/following.

        Add the current user as a follower of one or more artists or other
        Spotify users.

        Args:
            mtype (ItemType2): The request query parameter.
            ids (str): The request query parameter.
            body (MeFollowingRequest, optional): The request body parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Artist or
                user followed

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/following')
            .http_method(HttpMethodEnum.PUT)
            .query_param(Parameter()
                         .key('type')
                         .value(mtype)
                         .is_required(True))
            .query_param(Parameter()
                         .key('ids')
                         .value(ids)
                         .is_required(True))
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

    def unfollow_artists_users(self,
                               mtype,
                               ids,
                               body=None):
        """Does a DELETE request to /me/following.

        Remove the current user as a follower of one or more artists or other
        Spotify users.

        Args:
            mtype (ItemType3): The request query parameter.
            ids (str): The request query parameter.
            body (MeFollowingRequest1, optional): The request body parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Artist or
                user unfollowed

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/following')
            .http_method(HttpMethodEnum.DELETE)
            .query_param(Parameter()
                         .key('type')
                         .value(mtype)
                         .is_required(True))
            .query_param(Parameter()
                         .key('ids')
                         .value(ids)
                         .is_required(True))
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

    def check_current_user_follows(self,
                                   mtype,
                                   ids):
        """Does a GET request to /me/following/contains.

        Check to see if the current user is following one or more artists or
        other Spotify users.

        Args:
            mtype (ItemType3): The request query parameter.
            ids (str): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Array of
                booleans

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/following/contains')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('type')
                         .value(mtype)
                         .is_required(True))
            .query_param(Parameter()
                         .key('ids')
                         .value(ids)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def check_if_user_follows_playlist(self,
                                       playlist_id,
                                       ids):
        """Does a GET request to /playlists/{playlist_id}/followers/contains.

        Check to see if one or more Spotify users are following a specified
        playlist.

        Args:
            playlist_id (str): The request template parameter.
            ids (str): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Array of
                booleans

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/playlists/{playlist_id}/followers/contains')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('playlist_id')
                            .value(playlist_id)
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('ids')
                         .value(ids)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_users_top_artists(self,
                              time_range='medium_term',
                              limit=20,
                              offset=0):
        """Does a GET request to /me/top/artists.

        Get the current user's top artists based on calculated affinity.

        Args:
            time_range (str, optional): The request query parameter. Example:
                medium_term
            limit (int, optional): The request query parameter. Example: 20
            offset (int, optional): The request query parameter. Example: 0

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Pages of
                artists

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/top/artists')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('time_range')
                         .value(time_range))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('offset')
                         .value(offset))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PagingArtistObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_users_top_tracks(self,
                             time_range='medium_term',
                             limit=20,
                             offset=0):
        """Does a GET request to /me/top/tracks.

        Get the current user's top tracks based on calculated affinity.

        Args:
            time_range (str, optional): The request query parameter. Example:
                medium_term
            limit (int, optional): The request query parameter. Example: 20
            offset (int, optional): The request query parameter. Example: 0

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Pages of
                tracks

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/top/tracks')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('time_range')
                         .value(time_range))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('offset')
                         .value(offset))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PagingTrackObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()
