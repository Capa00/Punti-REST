from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

ROOT_URLCONF = 'punti.urls'

WSGI_APPLICATION = 'punti.wsgi.application'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/frontend/static/'
STATIC_ROOT = "/frontend/_static/"
