import os

from .base import *

SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = False

EMAIL_HOST = os.environ["EMAIL_HOST"]
EMAIL_PORT = os.environ["EMAIL_PORT"]

# Storage
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": os.environ.get("S3_BUCKET_NAME", "basegun-s3"),
            "endpoint_url": os.environ.get("S3_URL_ENDPOINT", None),
            "use_ssl": False,
        },
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
