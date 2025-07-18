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
from spotifywebapi.models.track_object import TrackObject
from spotifywebapi.models.many_tracks import ManyTracks
from spotifywebapi.models.paging_saved_track_object import PagingSavedTrackObject
from spotifywebapi.models.many_audio_features import ManyAudioFeatures
from spotifywebapi.models.audio_features_object import AudioFeaturesObject
from spotifywebapi.models.audio_analysis_object import AudioAnalysisObject
from spotifywebapi.models.recommendations_object import RecommendationsObject
from spotifywebapi.exceptions.unauthorized_exception import UnauthorizedException
from spotifywebapi.exceptions.forbidden_exception import ForbiddenException
from spotifywebapi.exceptions.too_many_requests_exception import TooManyRequestsException


class TracksApi(BaseApi):

    """A Controller to access Endpoints in the spotifywebapi API."""
    def __init__(self, config):
        super(TracksApi, self).__init__(config)

    def get_track(self,
                  id,
                  market=None):
        """Does a GET request to /tracks/{id}.

        Get Spotify catalog information for a single track identified by its
        unique Spotify ID.

        Args:
            id (str): The request template parameter.
            market (str, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A track

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/tracks/{id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('market')
                         .value(market))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(TrackObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_several_tracks(self,
                           ids,
                           market=None):
        """Does a GET request to /tracks.

        Get Spotify catalog information for multiple tracks based on their
        Spotify IDs.

        Args:
            ids (str): The request query parameter.
            market (str, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A set of
                tracks

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/tracks')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('ids')
                         .value(ids)
                         .is_required(True))
            .query_param(Parameter()
                         .key('market')
                         .value(market))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ManyTracks.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_users_saved_tracks(self,
                               market=None,
                               limit=20,
                               offset=0):
        """Does a GET request to /me/tracks.

        Get a list of the songs saved in the current Spotify user's 'Your
        Music' library.

        Args:
            market (str, optional): The request query parameter.
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
            .path('/me/tracks')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('market')
                         .value(market))
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
            .deserialize_into(PagingSavedTrackObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def save_tracks_user(self,
                         ids,
                         body=None):
        """Does a PUT request to /me/tracks.

        Save one or more tracks to the current user's 'Your Music' library.

        Args:
            ids (str): The request query parameter.
            body (MeTracksRequest, optional): The request body parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Track
                saved

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/tracks')
            .http_method(HttpMethodEnum.PUT)
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

    def remove_tracks_user(self,
                           ids,
                           body=None):
        """Does a DELETE request to /me/tracks.

        Remove one or more tracks from the current user's 'Your Music' library.

        Args:
            ids (str): The request query parameter.
            body (MeTracksRequest1, optional): The request body parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Track
                removed

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/tracks')
            .http_method(HttpMethodEnum.DELETE)
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

    def check_users_saved_tracks(self,
                                 ids):
        """Does a GET request to /me/tracks/contains.

        Check if one or more tracks is already saved in the current Spotify
        user's 'Your Music' library.

        Args:
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
            .path('/me/tracks/contains')
            .http_method(HttpMethodEnum.GET)
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

    def get_several_audio_features(self,
                                   ids):
        """Does a GET request to /audio-features.

        Get audio features for multiple tracks based on their Spotify IDs.

        Args:
            ids (str): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A set of
                audio features

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/audio-features')
            .http_method(HttpMethodEnum.GET)
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
            .deserialize_into(ManyAudioFeatures.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_audio_features(self,
                           id):
        """Does a GET request to /audio-features/{id}.

        Get audio feature information for a single track identified by its
        unique
        Spotify ID.

        Args:
            id (str): The request template parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Audio
                features for one track

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/audio-features/{id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AudioFeaturesObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_audio_analysis(self,
                           id):
        """Does a GET request to /audio-analysis/{id}.

        Get a low-level audio analysis for a track in the Spotify catalog. The
        audio analysis describes the track’s structure and musical content,
        including rhythm, pitch, and timbre.

        Args:
            id (str): The request template parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Audio
                analysis for one track

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/audio-analysis/{id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AudioAnalysisObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_recommendations(self,
                            limit=20,
                            market=None,
                            seed_artists=None,
                            seed_genres=None,
                            seed_tracks=None,
                            min_acousticness=None,
                            max_acousticness=None,
                            target_acousticness=None,
                            min_danceability=None,
                            max_danceability=None,
                            target_danceability=None,
                            min_duration_ms=None,
                            max_duration_ms=None,
                            target_duration_ms=None,
                            min_energy=None,
                            max_energy=None,
                            target_energy=None,
                            min_instrumentalness=None,
                            max_instrumentalness=None,
                            target_instrumentalness=None,
                            min_key=None,
                            max_key=None,
                            target_key=None,
                            min_liveness=None,
                            max_liveness=None,
                            target_liveness=None,
                            min_loudness=None,
                            max_loudness=None,
                            target_loudness=None,
                            min_mode=None,
                            max_mode=None,
                            target_mode=None,
                            min_popularity=None,
                            max_popularity=None,
                            target_popularity=None,
                            min_speechiness=None,
                            max_speechiness=None,
                            target_speechiness=None,
                            min_tempo=None,
                            max_tempo=None,
                            target_tempo=None,
                            min_time_signature=None,
                            max_time_signature=None,
                            target_time_signature=None,
                            min_valence=None,
                            max_valence=None,
                            target_valence=None):
        """Does a GET request to /recommendations.

        Recommendations are generated based on the available information for a
        given seed entity and matched against similar artists and tracks. If
        there is sufficient information about the provided seeds, a list of
        tracks will be returned together with pool size details.
        For artists and tracks that are very new or obscure there might not be
        enough data to generate a list of tracks.

        Args:
            limit (int, optional): The request query parameter. Example: 20
            market (str, optional): The request query parameter.
            seed_artists (str, optional): The request query parameter.
            seed_genres (str, optional): The request query parameter.
            seed_tracks (str, optional): The request query parameter.
            min_acousticness (float, optional): The request query parameter.
            max_acousticness (float, optional): The request query parameter.
            target_acousticness (float, optional): The request query parameter.
            min_danceability (float, optional): The request query parameter.
            max_danceability (float, optional): The request query parameter.
            target_danceability (float, optional): The request query parameter.
            min_duration_ms (int, optional): The request query parameter.
            max_duration_ms (int, optional): The request query parameter.
            target_duration_ms (int, optional): The request query parameter.
            min_energy (float, optional): The request query parameter.
            max_energy (float, optional): The request query parameter.
            target_energy (float, optional): The request query parameter.
            min_instrumentalness (float, optional): The request query
                parameter.
            max_instrumentalness (float, optional): The request query
                parameter.
            target_instrumentalness (float, optional): The request query
                parameter.
            min_key (int, optional): The request query parameter.
            max_key (int, optional): The request query parameter.
            target_key (int, optional): The request query parameter.
            min_liveness (float, optional): The request query parameter.
            max_liveness (float, optional): The request query parameter.
            target_liveness (float, optional): The request query parameter.
            min_loudness (float, optional): The request query parameter.
            max_loudness (float, optional): The request query parameter.
            target_loudness (float, optional): The request query parameter.
            min_mode (int, optional): The request query parameter.
            max_mode (int, optional): The request query parameter.
            target_mode (int, optional): The request query parameter.
            min_popularity (int, optional): The request query parameter.
            max_popularity (int, optional): The request query parameter.
            target_popularity (int, optional): The request query parameter.
            min_speechiness (float, optional): The request query parameter.
            max_speechiness (float, optional): The request query parameter.
            target_speechiness (float, optional): The request query parameter.
            min_tempo (float, optional): The request query parameter.
            max_tempo (float, optional): The request query parameter.
            target_tempo (float, optional): The request query parameter.
            min_time_signature (int, optional): The request query parameter.
            max_time_signature (int, optional): The request query parameter.
            target_time_signature (int, optional): The request query parameter.
            min_valence (float, optional): The request query parameter.
            max_valence (float, optional): The request query parameter.
            target_valence (float, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A set of
                recommendations

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/recommendations')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('market')
                         .value(market))
            .query_param(Parameter()
                         .key('seed_artists')
                         .value(seed_artists))
            .query_param(Parameter()
                         .key('seed_genres')
                         .value(seed_genres))
            .query_param(Parameter()
                         .key('seed_tracks')
                         .value(seed_tracks))
            .query_param(Parameter()
                         .key('min_acousticness')
                         .value(min_acousticness))
            .query_param(Parameter()
                         .key('max_acousticness')
                         .value(max_acousticness))
            .query_param(Parameter()
                         .key('target_acousticness')
                         .value(target_acousticness))
            .query_param(Parameter()
                         .key('min_danceability')
                         .value(min_danceability))
            .query_param(Parameter()
                         .key('max_danceability')
                         .value(max_danceability))
            .query_param(Parameter()
                         .key('target_danceability')
                         .value(target_danceability))
            .query_param(Parameter()
                         .key('min_duration_ms')
                         .value(min_duration_ms))
            .query_param(Parameter()
                         .key('max_duration_ms')
                         .value(max_duration_ms))
            .query_param(Parameter()
                         .key('target_duration_ms')
                         .value(target_duration_ms))
            .query_param(Parameter()
                         .key('min_energy')
                         .value(min_energy))
            .query_param(Parameter()
                         .key('max_energy')
                         .value(max_energy))
            .query_param(Parameter()
                         .key('target_energy')
                         .value(target_energy))
            .query_param(Parameter()
                         .key('min_instrumentalness')
                         .value(min_instrumentalness))
            .query_param(Parameter()
                         .key('max_instrumentalness')
                         .value(max_instrumentalness))
            .query_param(Parameter()
                         .key('target_instrumentalness')
                         .value(target_instrumentalness))
            .query_param(Parameter()
                         .key('min_key')
                         .value(min_key))
            .query_param(Parameter()
                         .key('max_key')
                         .value(max_key))
            .query_param(Parameter()
                         .key('target_key')
                         .value(target_key))
            .query_param(Parameter()
                         .key('min_liveness')
                         .value(min_liveness))
            .query_param(Parameter()
                         .key('max_liveness')
                         .value(max_liveness))
            .query_param(Parameter()
                         .key('target_liveness')
                         .value(target_liveness))
            .query_param(Parameter()
                         .key('min_loudness')
                         .value(min_loudness))
            .query_param(Parameter()
                         .key('max_loudness')
                         .value(max_loudness))
            .query_param(Parameter()
                         .key('target_loudness')
                         .value(target_loudness))
            .query_param(Parameter()
                         .key('min_mode')
                         .value(min_mode))
            .query_param(Parameter()
                         .key('max_mode')
                         .value(max_mode))
            .query_param(Parameter()
                         .key('target_mode')
                         .value(target_mode))
            .query_param(Parameter()
                         .key('min_popularity')
                         .value(min_popularity))
            .query_param(Parameter()
                         .key('max_popularity')
                         .value(max_popularity))
            .query_param(Parameter()
                         .key('target_popularity')
                         .value(target_popularity))
            .query_param(Parameter()
                         .key('min_speechiness')
                         .value(min_speechiness))
            .query_param(Parameter()
                         .key('max_speechiness')
                         .value(max_speechiness))
            .query_param(Parameter()
                         .key('target_speechiness')
                         .value(target_speechiness))
            .query_param(Parameter()
                         .key('min_tempo')
                         .value(min_tempo))
            .query_param(Parameter()
                         .key('max_tempo')
                         .value(max_tempo))
            .query_param(Parameter()
                         .key('target_tempo')
                         .value(target_tempo))
            .query_param(Parameter()
                         .key('min_time_signature')
                         .value(min_time_signature))
            .query_param(Parameter()
                         .key('max_time_signature')
                         .value(max_time_signature))
            .query_param(Parameter()
                         .key('target_time_signature')
                         .value(target_time_signature))
            .query_param(Parameter()
                         .key('min_valence')
                         .value(min_valence))
            .query_param(Parameter()
                         .key('max_valence')
                         .value(max_valence))
            .query_param(Parameter()
                         .key('target_valence')
                         .value(target_valence))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(RecommendationsObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()
