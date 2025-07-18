# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapi.api_helper import APIHelper
from spotifywebapi.models.audiobook_base import AudiobookBase
from spotifywebapi.models.chapter_restriction_object import ChapterRestrictionObject
from spotifywebapi.models.external_url_object import ExternalUrlObject
from spotifywebapi.models.image_object import ImageObject
from spotifywebapi.models.resume_point_object import ResumePointObject


class ChapterObject(object):

    """Implementation of the 'ChapterObject' model.

    Attributes:
        audio_preview_url (str): A URL to a 30 second preview (MP3 format) of
            the chapter. `null` if not available.
        available_markets (List[str]): A list of the countries in which the
            chapter can be played, identified by their [ISO 3166-1
            alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code.
        chapter_number (int): The number of the chapter
        description (str): A description of the chapter. HTML tags are
            stripped away from this field, use `html_description` field in
            case HTML tags are needed.
        html_description (str): A description of the chapter. This field may
            contain HTML tags.
        duration_ms (int): The chapter length in milliseconds.
        explicit (bool): Whether or not the chapter has explicit content (true
            = yes it does; false = no it does not OR unknown).
        external_urls (ExternalUrlObject): External URLs for this chapter.
        href (str): A link to the Web API endpoint providing full details of
            the chapter.
        id (str): The [Spotify
            ID](/documentation/web-api/concepts/spotify-uris-ids) for the
            chapter.
        images (List[ImageObject]): The cover art for the chapter in various
            sizes, widest first.
        is_playable (bool): True if the chapter is playable in the given
            market. Otherwise false.
        languages (List[str]): A list of the languages used in the chapter,
            identified by their [ISO
            639-1](https://en.wikipedia.org/wiki/ISO_639) code.
        name (str): The name of the chapter.
        release_date (str): The date the chapter was first released, for
            example `"1981-12-15"`. Depending on the precision, it might be
            shown as `"1981"` or `"1981-12"`.
        release_date_precision (ReleaseDatePrecision): The precision with
            which `release_date` value is known.
        resume_point (ResumePointObject): The user's most recent position in
            the chapter. Set if the supplied access token is a user token and
            has the scope 'user-read-playback-position'.
        mtype (str): The object type.
        uri (str): The [Spotify
            URI](/documentation/web-api/concepts/spotify-uris-ids) for the
            chapter.
        restrictions (ChapterRestrictionObject): Included in the response when
            a content restriction is applied.
        audiobook (AudiobookBase): The audiobook for which the chapter belongs.
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "audio_preview_url": 'audio_preview_url',
        "chapter_number": 'chapter_number',
        "description": 'description',
        "html_description": 'html_description',
        "duration_ms": 'duration_ms',
        "explicit": 'explicit',
        "external_urls": 'external_urls',
        "href": 'href',
        "id": 'id',
        "images": 'images',
        "is_playable": 'is_playable',
        "languages": 'languages',
        "name": 'name',
        "release_date": 'release_date',
        "release_date_precision": 'release_date_precision',
        "mtype": 'type',
        "uri": 'uri',
        "audiobook": 'audiobook',
        "available_markets": 'available_markets',
        "resume_point": 'resume_point',
        "restrictions": 'restrictions'
    }

    _optionals = [
        'available_markets',
        'resume_point',
        'restrictions',
    ]

    _nullables = [
        'audio_preview_url',
    ]

    def __init__(self,
                 audio_preview_url=None,
                 chapter_number=None,
                 description=None,
                 html_description=None,
                 duration_ms=None,
                 explicit=None,
                 external_urls=None,
                 href=None,
                 id=None,
                 images=None,
                 is_playable=None,
                 languages=None,
                 name=None,
                 release_date=None,
                 release_date_precision=None,
                 uri=None,
                 audiobook=None,
                 available_markets=APIHelper.SKIP,
                 resume_point=APIHelper.SKIP,
                 restrictions=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ChapterObject class"""

        # Initialize members of the class
        self.audio_preview_url = audio_preview_url 
        if available_markets is not APIHelper.SKIP:
            self.available_markets = available_markets 
        self.chapter_number = chapter_number 
        self.description = description 
        self.html_description = html_description 
        self.duration_ms = duration_ms 
        self.explicit = explicit 
        self.external_urls = external_urls 
        self.href = href 
        self.id = id 
        self.images = images 
        self.is_playable = is_playable 
        self.languages = languages 
        self.name = name 
        self.release_date = release_date 
        self.release_date_precision = release_date_precision 
        if resume_point is not APIHelper.SKIP:
            self.resume_point = resume_point 
        self.mtype = 'episode' 
        self.uri = uri 
        if restrictions is not APIHelper.SKIP:
            self.restrictions = restrictions 
        self.audiobook = audiobook 

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
        audio_preview_url = dictionary.get("audio_preview_url") if dictionary.get("audio_preview_url") else None
        chapter_number = dictionary.get("chapter_number") if dictionary.get("chapter_number") else None
        description = dictionary.get("description") if dictionary.get("description") else None
        html_description = dictionary.get("html_description") if dictionary.get("html_description") else None
        duration_ms = dictionary.get("duration_ms") if dictionary.get("duration_ms") else None
        explicit = dictionary.get("explicit") if "explicit" in dictionary.keys() else None
        external_urls = ExternalUrlObject.from_dictionary(dictionary.get('external_urls')) if dictionary.get('external_urls') else None
        href = dictionary.get("href") if dictionary.get("href") else None
        id = dictionary.get("id") if dictionary.get("id") else None
        images = None
        if dictionary.get('images') is not None:
            images = [ImageObject.from_dictionary(x) for x in dictionary.get('images')]
        is_playable = dictionary.get("is_playable") if "is_playable" in dictionary.keys() else None
        languages = dictionary.get("languages") if dictionary.get("languages") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        release_date = dictionary.get("release_date") if dictionary.get("release_date") else None
        release_date_precision = dictionary.get("release_date_precision") if dictionary.get("release_date_precision") else None
        uri = dictionary.get("uri") if dictionary.get("uri") else None
        audiobook = AudiobookBase.from_dictionary(dictionary.get('audiobook')) if dictionary.get('audiobook') else None
        available_markets = dictionary.get("available_markets") if dictionary.get("available_markets") else APIHelper.SKIP
        resume_point = ResumePointObject.from_dictionary(dictionary.get('resume_point')) if 'resume_point' in dictionary.keys() else APIHelper.SKIP
        restrictions = ChapterRestrictionObject.from_dictionary(dictionary.get('restrictions')) if 'restrictions' in dictionary.keys() else APIHelper.SKIP
        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items() if k not in cls._names.values()},
            unboxing_function=lambda value: value)
        # Return an object of this model
        return cls(audio_preview_url,
                   chapter_number,
                   description,
                   html_description,
                   duration_ms,
                   explicit,
                   external_urls,
                   href,
                   id,
                   images,
                   is_playable,
                   languages,
                   name,
                   release_date,
                   release_date_precision,
                   uri,
                   audiobook,
                   available_markets,
                   resume_point,
                   restrictions,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'audio_preview_url={self.audio_preview_url!r}, '
                f'available_markets={(self.available_markets if hasattr(self, "available_markets") else None)!r}, '
                f'chapter_number={self.chapter_number!r}, '
                f'description={self.description!r}, '
                f'html_description={self.html_description!r}, '
                f'duration_ms={self.duration_ms!r}, '
                f'explicit={self.explicit!r}, '
                f'external_urls={self.external_urls!r}, '
                f'href={self.href!r}, '
                f'id={self.id!r}, '
                f'images={self.images!r}, '
                f'is_playable={self.is_playable!r}, '
                f'languages={self.languages!r}, '
                f'name={self.name!r}, '
                f'release_date={self.release_date!r}, '
                f'release_date_precision={self.release_date_precision!r}, '
                f'resume_point={(self.resume_point if hasattr(self, "resume_point") else None)!r}, '
                f'mtype={self.mtype!r}, '
                f'uri={self.uri!r}, '
                f'restrictions={(self.restrictions if hasattr(self, "restrictions") else None)!r}, '
                f'audiobook={self.audiobook!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'audio_preview_url={self.audio_preview_url!s}, '
                f'available_markets={(self.available_markets if hasattr(self, "available_markets") else None)!s}, '
                f'chapter_number={self.chapter_number!s}, '
                f'description={self.description!s}, '
                f'html_description={self.html_description!s}, '
                f'duration_ms={self.duration_ms!s}, '
                f'explicit={self.explicit!s}, '
                f'external_urls={self.external_urls!s}, '
                f'href={self.href!s}, '
                f'id={self.id!s}, '
                f'images={self.images!s}, '
                f'is_playable={self.is_playable!s}, '
                f'languages={self.languages!s}, '
                f'name={self.name!s}, '
                f'release_date={self.release_date!s}, '
                f'release_date_precision={self.release_date_precision!s}, '
                f'resume_point={(self.resume_point if hasattr(self, "resume_point") else None)!s}, '
                f'mtype={self.mtype!s}, '
                f'uri={self.uri!s}, '
                f'restrictions={(self.restrictions if hasattr(self, "restrictions") else None)!s}, '
                f'audiobook={self.audiobook!s}, '
                f'additional_properties={self.additional_properties!s})')
