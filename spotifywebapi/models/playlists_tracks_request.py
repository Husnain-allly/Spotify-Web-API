# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapi.api_helper import APIHelper


class PlaylistsTracksRequest(object):

    """Implementation of the 'Playlists Tracks Request' model.

    Attributes:
        uris (List[str]): A JSON array of the [Spotify
            URIs](/documentation/web-api/concepts/spotify-uris-ids) to add.
            For example: `{"uris":
            ["spotify:track:4iV5W9uYEdYUVa79Axb7Rh","spotify:track:1301WleyT98M
            SxVHPZCA6M", "spotify:episode:512ojhOuo1ktJprKbVcKyQ"]}`<br/>A
            maximum of 100 items can be added in one request. _**Note**: if
            the `uris` parameter is present in the query string, any URIs
            listed here in the body will be ignored._
        position (int): The position to insert the items, a zero-based index.
            For example, to insert the items in the first position:
            `position=0` ; to insert the items in the third position:
            `position=2`. If omitted, the items will be appended to the
            playlist. Items are added in the order they appear in the uris
            array. For example: `{"uris":
            ["spotify:track:4iV5W9uYEdYUVa79Axb7Rh","spotify:track:1301WleyT98M
            SxVHPZCA6M"], "position": 3}`
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uris": 'uris',
        "position": 'position'
    }

    _optionals = [
        'uris',
        'position',
    ]

    def __init__(self,
                 uris=APIHelper.SKIP,
                 position=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the PlaylistsTracksRequest class"""

        # Initialize members of the class
        if uris is not APIHelper.SKIP:
            self.uris = uris 
        if position is not APIHelper.SKIP:
            self.position = position 

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
        uris = dictionary.get("uris") if dictionary.get("uris") else APIHelper.SKIP
        position = dictionary.get("position") if dictionary.get("position") else APIHelper.SKIP
        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items() if k not in cls._names.values()},
            unboxing_function=lambda value: value)
        # Return an object of this model
        return cls(uris,
                   position,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'uris={(self.uris if hasattr(self, "uris") else None)!r}, '
                f'position={(self.position if hasattr(self, "position") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'uris={(self.uris if hasattr(self, "uris") else None)!s}, '
                f'position={(self.position if hasattr(self, "position") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
