from __future__ import unicode_literals

from django.db import models
from eventbrite import Eventbrite


def get_categories():
    """
    This returns all categories from the eventbrite API

    :return:
    """
    eventbrite = Eventbrite('5NGHYUHHECWB3CBRXKY2')
    categories = eventbrite.get_categories()

    return get_events(categories)


def get_events(categories):
    """
    Given a set of categories, returns relevant events

    :param categories:
    """
    eventbrite = Eventbrite('5NGHYUHHECWB3CBRXKY2')
    category_ids = []
    for category in categories['categories']:
        category_ids = category['id']

    events = eventbrite.event_search(**{'categories': 108})
    return events
