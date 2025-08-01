# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapi.api_helper import APIHelper
from spotifywebapi.models.show_base import ShowBase


class ManySimplifiedShows(object):

    """Implementation of the 'ManySimplifiedShows' model.

    Attributes:
        shows (List[ShowBase]): The model property of type List[ShowBase].
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "shows": 'shows'
    }

    def __init__(self,
                 shows=None,
                 additional_properties=None):
        """Constructor for the ManySimplifiedShows class"""

        # Initialize members of the class
        self.shows = shows 

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
        shows = None
        if dictionary.get('shows') is not None:
            shows = [ShowBase.from_dictionary(x) for x in dictionary.get('shows')]
        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items() if k not in cls._names.values()},
            unboxing_function=lambda value: value)
        # Return an object of this model
        return cls(shows,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'shows={self.shows!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'shows={self.shows!s}, '
                f'additional_properties={self.additional_properties!s})')
