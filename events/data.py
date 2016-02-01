from __future__ import unicode_literals

from django.conf import settings
from eventbrite import Eventbrite


class Category:
    def __init__(self):
        self.eventbrite = Eventbrite(settings.EVENTBRITE_API_KEY)

    def all(self):
        """
        This returns all categories from the eventbrite API

        :return:
        :return: List of categories
        """
        eventbrite_categories = self.eventbrite.get_categories()
        if eventbrite_categories.status_code == 200:
            return eventbrite_categories['categories']
        else:
            return None

    def get(self, category_id):
        """
        Given the id of a category, returns that eventbrite category object

        :param category_id:
        :return:
        """
        data = self.eventbrite.get_category(category_id)
        if data.status_code == 200:
            return data
        else:
            return None

    def get_multiple(self, category_ids):
        """
        Returns category objects for category ids given

        :param category_ids:
        :return:
        """
        categories = []
        for category_id in category_ids:
            categories.append(self.get(category_id))

        return categories


class Event:
    def __init__(self):
        self.eventbrite = Eventbrite(settings.EVENTBRITE_API_KEY)

    def get(self, events_id):
        """
        Given an eventbrite ID, returns the event object

        :param events_id:
        :return:
        """

        data = self.eventbrite.get_event(events_id)
        if data.status_code == 200:
            return data
        else:
            return None

    def get_multiple(self, category_ids, page_number):
        """
        Given a set of categories, returns relevant events
        :param category_ids:
        :param page_number:
        :return:
        """

        data = self.eventbrite.event_search(**{'page': page_number, 'categories': category_ids})
        if data.status_code == 200:
            return data
        else:
            return None
