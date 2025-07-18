# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapi.api_helper import APIHelper


class MePlayerPlayRequest(object):

    """Implementation of the 'Me Player Play Request' model.

    Attributes:
        context_uri (str): Optional. Spotify URI of the context to play. Valid
            contexts are albums, artists & playlists.
            `{context_uri:"spotify:album:1Je1IMUlBXcx1Fz0WE7oPT"}`
        uris (List[str]): Optional. A JSON array of the Spotify track URIs to
            play. For example: `{"uris":
            ["spotify:track:4iV5W9uYEdYUVa79Axb7Rh",
            "spotify:track:1301WleyT98MSxVHPZCA6M"]}`
        offset (Any): Optional. Indicates from where in the context playback
            should start. Only available when context_uri corresponds to an
            album or playlist object "position" is zero based and can’t be
            negative. Example: `"offset": {"position": 5}` "uri" is a string
            representing the uri of the item to start at. Example: `"offset":
            {"uri": "spotify:track:1301WleyT98MSxVHPZCA6M"}`
        position_ms (int): Indicates from what position to start playback.
            Must be a positive number. Passing in a position that is greater
            than the length of the track will cause the player to start
            playing the next song.
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "context_uri": 'context_uri',
        "uris": 'uris',
        "offset": 'offset',
        "position_ms": 'position_ms'
    }

    _optionals = [
        'context_uri',
        'uris',
        'offset',
        'position_ms',
    ]

    def __init__(self,
                 context_uri=APIHelper.SKIP,
                 uris=APIHelper.SKIP,
                 offset=APIHelper.SKIP,
                 position_ms=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the MePlayerPlayRequest class"""

        # Initialize members of the class
        if context_uri is not APIHelper.SKIP:
            self.context_uri = context_uri 
        if uris is not APIHelper.SKIP:
            self.uris = uris 
        if offset is not APIHelper.SKIP:
            self.offset = offset 
        if position_ms is not APIHelper.SKIP:
            self.position_ms = position_ms 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        context_uri = dictionary.get("context_uri") if dictionary.get("context_uri") else APIHelper.SKIP
        uris = dictionary.get("uris") if dictionary.get("uris") else APIHelper.SKIP
        offset = dictionary.get("offset") if dictionary.get("offset") else APIHelper.SKIP
        position_ms = dictionary.get("position_ms") if dictionary.get("position_ms") else APIHelper.SKIP
        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items() if k not in cls._names.values()},
            unboxing_function=lambda value: value)
        # Return an object of this model
        return cls(context_uri,
                   uris,
                   offset,
                   position_ms,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'context_uri={(self.context_uri if hasattr(self, "context_uri") else None)!r}, '
                f'uris={(self.uris if hasattr(self, "uris") else None)!r}, '
                f'offset={(self.offset if hasattr(self, "offset") else None)!r}, '
                f'position_ms={(self.position_ms if hasattr(self, "position_ms") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'context_uri={(self.context_uri if hasattr(self, "context_uri") else None)!s}, '
                f'uris={(self.uris if hasattr(self, "uris") else None)!s}, '
                f'offset={(self.offset if hasattr(self, "offset") else None)!s}, '
                f'position_ms={(self.position_ms if hasattr(self, "position_ms") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
