from __future__ import absolute_import

import os

from celery import Celery
from kloutmachine.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kloutmachine.settings.development")

app = Celery("kloutmachine")

app.config_from_object("kloutmachine.settings.development", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)