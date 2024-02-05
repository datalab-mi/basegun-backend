import os

from .base import *

SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = False

EMAIL_HOST = os.environ["EMAIL_HOST"]
EMAIL_PORT = os.environ["EMAIL_PORT"]
