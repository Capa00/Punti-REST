"""
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEBUG = True
SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
gettext = lambda s: s
LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ('en-us', gettext('English')),
]

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

from .auth import *
from .direcotries import *
from .apps import *
from .middleware import *
from .environments import *
from .common import *
from .databases import *
from .admin_site import *
from .templates import *

from .api import *
