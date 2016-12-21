from ac5.base_settings import *

DEBUG=True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "dev.db",
    }
}

ALLOWED_HOSTS = [
    "localhost",
]



