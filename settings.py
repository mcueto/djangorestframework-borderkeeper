import datetime
import base64

from django.conf import settings
from rest_framework.settings import APISettings


USER_SETTINGS = getattr(settings, 'BORDERKEEPER', None)

DEFAULTS = {
}

# List of settings that may be in string import notation.
IMPORT_STRINGS = (
)

api_settings = APISettings(USER_SETTINGS, DEFAULTS)
