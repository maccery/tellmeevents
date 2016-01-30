from __future__ import unicode_literals

from django.db import models
from eventbrite import Eventbrite


def get_categories():
    eventbrite = Eventbrite('5NGHYUHHECWB3CBRXKY2')
    categories = eventbrite.get_categories()
    return categories