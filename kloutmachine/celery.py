from __future__ import absolute_import

import os

from celery import Celery
from Kloutmachine.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Kloutmachine.settings.development")

app = Celery("Kloutmachine")

app.config_from_object("Kloutmachine.settings.development", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)