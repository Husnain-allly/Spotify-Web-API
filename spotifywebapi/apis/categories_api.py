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
from spotifywebapi.models.paged_categories import PagedCategories
from spotifywebapi.models.category_object import CategoryObject
from spotifywebapi.exceptions.unauthorized_exception import UnauthorizedException
from spotifywebapi.exceptions.forbidden_exception import ForbiddenException
from spotifywebapi.exceptions.too_many_requests_exception import TooManyRequestsException


class CategoriesApi(BaseApi):

    """A Controller to access Endpoints in the spotifywebapi API."""
    def __init__(self, config):
        super(CategoriesApi, self).__init__(config)

    def get_categories(self,
                       locale=None,
                       limit=20,
                       offset=0):
        """Does a GET request to /browse/categories.

        Get a list of categories used to tag items in Spotify (on, for
        example, the Spotify player’s “Browse” tab).

        Args:
            locale (str, optional): The request query parameter.
            limit (int, optional): The request query parameter. Example: 20
            offset (int, optional): The request query parameter. Example: 0

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A paged
                set of categories

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/browse/categories')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('locale')
                         .value(locale))
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
            .deserialize_into(PagedCategories.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_a_category(self,
                       category_id,
                       locale=None):
        """Does a GET request to /browse/categories/{category_id}.

        Get a single category used to tag items in Spotify (on, for example,
        the Spotify player’s “Browse” tab).

        Args:
            category_id (str): The request template parameter.
            locale (str, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A category

        Raises:
            ApiException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/browse/categories/{category_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('category_id')
                            .value(category_id)
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('locale')
                         .value(locale))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CategoryObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()
