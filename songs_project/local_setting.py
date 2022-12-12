# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j4x(f)#evs147pma%-r0q0kpe048kv7z&9ab2nrgr@wc8#%#u1'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'songs_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password',
    }
}