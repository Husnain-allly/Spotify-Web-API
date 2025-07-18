# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapi.api_helper import APIHelper
from spotifywebapi.models.show_base import ShowBase


class SavedShowObject(object):

    """Implementation of the 'SavedShowObject' model.

    Attributes:
        added_at (datetime): The date and time the show was saved. Timestamps
            are returned in ISO 8601 format as Coordinated Universal Time
            (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ. If the time is
            imprecise (for example, the date/time of an album release), an
            additional field indicates the precision; see for example,
            release_date in an album object.
        show (ShowBase): Information about the show.
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "added_at": 'added_at',
        "show": 'show'
    }

    _optionals = [
        'added_at',
        'show',
    ]

    def __init__(self,
                 added_at=APIHelper.SKIP,
                 show=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SavedShowObject class"""

        # Initialize members of the class
        if added_at is not APIHelper.SKIP:
            self.added_at = APIHelper.apply_datetime_converter(added_at, APIHelper.RFC3339DateTime) if added_at else None 
        if show is not APIHelper.SKIP:
            self.show = show 

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
        added_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("added_at")).datetime if dictionary.get("added_at") else APIHelper.SKIP
        show = ShowBase.from_dictionary(dictionary.get('show')) if 'show' in dictionary.keys() else APIHelper.SKIP
        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items() if k not in cls._names.values()},
            unboxing_function=lambda value: value)
        # Return an object of this model
        return cls(added_at,
                   show,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'added_at={(self.added_at if hasattr(self, "added_at") else None)!r}, '
                f'show={(self.show if hasattr(self, "show") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'added_at={(self.added_at if hasattr(self, "added_at") else None)!s}, '
                f'show={(self.show if hasattr(self, "show") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
