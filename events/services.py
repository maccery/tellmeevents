from __future__ import unicode_literals

from django.conf import settings
from eventbrite import Eventbrite


class Category:
    def __init__(self):
        self.eventbrite = Eventbrite(settings.EVENTBRITE_API_KEY)

    def get_all_categories(self):
        """
        This returns all categories from the eventbrite API

        :return:
        :return: List of categories
        """
        return self.eventbrite.get_categories()['categories']

    def get_category(self, category_id):
        """
        Given the id of a category, returns that eventbrite category object

        :param category_id:
        :return:
        """
        return self.eventbrite.get_category(category_id)

    def get_categories(self, category_ids):
        """
        Returns category objects for category ids given

        :param category_ids:
        :return:
        """
        categories = []
        for category_id in category_ids:
            categories.append(self.get_category(category_id))

        return categories


class Event:
    def __init__(self):
        self.eventbrite = Eventbrite(settings.EVENTBRITE_API_KEY)

    def get_event(self, events_id):
        """
        Given an eventbrite ID, returns the event object

        :param events_id:
        :return:
        """
        return self.get_event(events_id)

    def get_events(self, category_ids, page_number):
        """
        Given a set of categories, returns relevant events

        :return: List of events
        :param categories:
        """

        return self.eventbrite.event_search(**{'page': page_number, 'categories': category_ids})
