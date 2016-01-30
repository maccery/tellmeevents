from __future__ import unicode_literals

from django.db import models
from eventbrite import Eventbrite

eventbrite = Eventbrite('5NGHYUHHECWB3CBRXKY2')

def get_categories():
    """
    This returns all categories from the eventbrite API

    :return: List of categories
    """
    eventbrite = Eventbrite('5NGHYUHHECWB3CBRXKY2')
    return eventbrite.get_categories()


def get_events(category_ids):
    """
    Given a set of categories, returns relevant events

    :return: List of events
    :param categories:
    """

    return eventbrite.event_search(**{'categories': category_ids})
