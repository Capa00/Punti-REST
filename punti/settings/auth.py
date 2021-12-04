# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8b(a(^v&f#is4b+0$&#mpki38$i+#d3=35!^r#lww5%7*4slh2'

ALLOWED_HOSTS = []

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]