from my_blog.settings import *  # NOQA

INTERNAL_IPS = ['127.0.0.1']
INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# config cache to use redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # 'LOCATION': 'redis://127.0.0.1:6379/11',
        'LOCATION': 'redis://172.16.15.203:6379/11',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            # 'PASSWORD': 'my secret',
            'SOCKET_CONNECT_TIMEOUT': 5,
            'SOCKET_TIMEOUT': 5,
            'COLLECTION_POOL_KWARGS': {'max_collections': 100}
        }
    }
}

# config session to use redis
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

STATIC_ROOT = None
MEDIA_ROOT = MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
