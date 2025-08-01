# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapi.api_helper import APIHelper
from spotifywebapi.models.artist_object import ArtistObject
from spotifywebapi.models.cursor_object import CursorObject


class CursorPagingSimplifiedArtistObject(object):

    """Implementation of the 'CursorPagingSimplifiedArtistObject' model.

    Attributes:
        href (str): A link to the Web API endpoint returning the full result
            of the request.
        limit (int): The maximum number of items in the response (as set in
            the query or by default).
        next (str): URL to the next page of items. ( `null` if none)
        cursors (CursorObject): The cursors used to find the next set of items.
        total (int): The total number of items available to return.
        items (List[ArtistObject]): The model property of type
            List[ArtistObject].
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "href": 'href',
        "limit": 'limit',
        "next": 'next',
        "cursors": 'cursors',
        "total": 'total',
        "items": 'items'
    }

    _optionals = [
        'href',
        'limit',
        'next',
        'cursors',
        'total',
        'items',
    ]

    def __init__(self,
                 href=APIHelper.SKIP,
                 limit=APIHelper.SKIP,
                 next=APIHelper.SKIP,
                 cursors=APIHelper.SKIP,
                 total=APIHelper.SKIP,
                 items=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CursorPagingSimplifiedArtistObject class"""

        # Initialize members of the class
        if href is not APIHelper.SKIP:
            self.href = href 
        if limit is not APIHelper.SKIP:
            self.limit = limit 
        if next is not APIHelper.SKIP:
            self.next = next 
        if cursors is not APIHelper.SKIP:
            self.cursors = cursors 
        if total is not APIHelper.SKIP:
            self.total = total 
        if items is not APIHelper.SKIP:
            self.items = items 

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
        href = dictionary.get("href") if dictionary.get("href") else APIHelper.SKIP
        limit = dictionary.get("limit") if dictionary.get("limit") else APIHelper.SKIP
        next = dictionary.get("next") if dictionary.get("next") else APIHelper.SKIP
        cursors = CursorObject.from_dictionary(dictionary.get('cursors')) if 'cursors' in dictionary.keys() else APIHelper.SKIP
        total = dictionary.get("total") if dictionary.get("total") else APIHelper.SKIP
        items = None
        if dictionary.get('items') is not None:
            items = [ArtistObject.from_dictionary(x) for x in dictionary.get('items')]
        else:
            items = APIHelper.SKIP
        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items() if k not in cls._names.values()},
            unboxing_function=lambda value: value)
        # Return an object of this model
        return cls(href,
                   limit,
                   next,
                   cursors,
                   total,
                   items,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'href={(self.href if hasattr(self, "href") else None)!r}, '
                f'limit={(self.limit if hasattr(self, "limit") else None)!r}, '
                f'next={(self.next if hasattr(self, "next") else None)!r}, '
                f'cursors={(self.cursors if hasattr(self, "cursors") else None)!r}, '
                f'total={(self.total if hasattr(self, "total") else None)!r}, '
                f'items={(self.items if hasattr(self, "items") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'href={(self.href if hasattr(self, "href") else None)!s}, '
                f'limit={(self.limit if hasattr(self, "limit") else None)!s}, '
                f'next={(self.next if hasattr(self, "next") else None)!s}, '
                f'cursors={(self.cursors if hasattr(self, "cursors") else None)!s}, '
                f'total={(self.total if hasattr(self, "total") else None)!s}, '
                f'items={(self.items if hasattr(self, "items") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
