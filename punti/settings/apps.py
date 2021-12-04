# Application definition

MY_APPS = [
    'scheduler',
    'entities',
    'simulations',
    'web.pcms',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    *MY_APPS,

    'rest_framework',
    'rangefilter',
]
