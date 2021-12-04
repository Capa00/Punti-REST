from punti.settings import BASE_DIR, ENV

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },

    'mongo': {
        'ENGINE': 'djongo',
        'NAME': 'punti',
        'CLIENT': {
            'host': ENV['mongo']['host'],
            'port': ENV['mongo']['port'],
        },
    },

}

DATABASE_ROUTERS = ['punti.routers.MongoRouter']

