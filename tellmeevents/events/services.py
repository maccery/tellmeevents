from __future__ import unicode_literals

from django.db import models
from eventbrite import Eventbrite


def get_all_categories():
    """
    This returns all categories from the eventbrite API

    :return:
    :return: List of categories
    """
    eventbrite = Eventbrite('5NGHYUHHECWB3CBRXKY2')
    return eventbrite.get_categories()


def get_category(category_id):
    """
    Given the id of a category, returns that eventbrite category object

    :param category_id:
    :return:
    """
    eventbrite = Eventbrite('5NGHYUHHECWB3CBRXKY2')
    return eventbrite.get_category(category_id)


def get_event(events_id):
    eventbrite = Eventbrite('5NGHYUHHECWB3CBRXKY2')
    return eventbrite.get_event(events_id)


def get_events(category_ids, page_number):
    """
    Given a set of categories, returns relevant events

    :return: List of events
    :param categories:
    """
    eventbrite = Eventbrite('5NGHYUHHECWB3CBRXKY2')
    return eventbrite.event_search(**{'page': page_number, 'categories': category_ids})
