"""Constants for the Mealie integration."""

import logging

from awesomeversion import AwesomeVersion

DOMAIN = "mealie-meal-times"

LOGGER = logging.getLogger(__package__)

ATTR_START_DATE = "start_date"
ATTR_END_DATE = "end_date"
ATTR_RECIPE_ID = "recipe_id"
ATTR_URL = "url"
ATTR_INCLUDE_TAGS = "include_tags"
ATTR_ENTRY_TYPE = "entry_type"
ATTR_NOTE_TITLE = "note_title"
ATTR_NOTE_TEXT = "note_text"
ATTR_SEARCH_TERMS = "search_terms"
ATTR_RESULT_LIMIT = "result_limit"

MIN_REQUIRED_MEALIE_VERSION = AwesomeVersion("v1.0.0")


BREAKFAST_TIME = "Lunch Time"
LUNCH_TIME = "Lunch Time"
DINNER_TIME = "Lunch Time"
SIDE_TIME = "Side Time"
