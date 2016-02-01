from django.test import TestCase, Client
import unittest

from mock import patch, MagicMock
from data import Event, Category


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    """
    Tests to make sure that the correct Eventbrite API is called for each of our pages
    """

    @patch('eventbrite.Eventbrite.get_categories')
    def test_homepage(self, mock_get_all_categories):
        mock_get_all_categories.return_value = MagicMock()
        self.client.get('/', {})
        mock_get_all_categories.assert_called_once_with()

    @patch('eventbrite.Eventbrite.event_search')
    def test_search(self, mock_event_search):
        mock_event_search.return_value = MagicMock(status_code=200)
        category_ids = ['2', '4', '5']

        self.client.get('/results',
                        {"category1": category_ids[0], "category2": category_ids[1], "category3": category_ids[2]})

        # Check that this function is actually called with the correct data
        mock_event_search.assert_called_once_with(**{"page": 1, "categories": category_ids})

    @patch('eventbrite.Eventbrite.event_search')
    def test_pagination(self, mock_event_search):
        for page_number in range(1, 4):
            mock_event_search.return_value = MagicMock(status_code=200)
            category_ids = ['2', '4', '5']
            self.client.get('/results/' + str(page_number) + '/',
                            {"category1": category_ids[0], "category2": category_ids[1], "category3": category_ids[2]})

            mock_event_search.assert_called_with(**{"page": str(page_number), "categories": category_ids})

    @patch('eventbrite.Eventbrite.get_event')
    def test_get_event(self, mock_get_event):
        mock_get_event.return_value = MagicMock()

        self.client.get('/event/32/', {})
        mock_get_event.assert_called_once_with('32')

    """
    Tests to check if the Eventbrite API errors, that we return None
    """

    @patch('eventbrite.Eventbrite.get_event')
    def test_get_event_error(self, mock_get_event):
        mock_get_event.return_value = MagicMock(status_code=500)
        event = Event().get_event(1)
        assert (event is None)

    @patch('eventbrite.Eventbrite.get_categories')
    def test_get_event_error(self, get_categories):
        get_categories.return_value = MagicMock(status_code=500)
        categories = Category().get_all_categories()
        assert (categories is None)

    @patch('eventbrite.Eventbrite.get_category')
    def test_get_event_error(self, mock_get_category):
        mock_get_category.return_value = MagicMock(status_code=500)
        category = Category().get_category(2)
        assert (category is None)

    @patch('eventbrite.Eventbrite.get_categories')
    def test_get_event_error(self, get_categories):
        get_categories.return_value = MagicMock(status_code=500)
        categories = Category().get_categories([])
        assert (categories is None)

    @patch('eventbrite.Eventbrite.event_search')
    def test_get_event_error(self, mock_event_search):
        mock_event_search.return_value = MagicMock(status_code=500)
        event = Event().get_events([], 1)
        assert (event is None)


class FunctionalTests(TestCase):
    """
    Tests that check that an error message is displayed if we have nothing returned
    """

    @patch('events.data.Category.get_all_categories')
    def test_homepage_no_categories_found(self, mock_get_all_categories):
        mock_get_all_categories.return_value = None
        response = self.client.get('/', {})
        self.assertTemplateUsed(response, 'events/no_categories_found.html')

    @patch('events.data.Event.get_event')
    def test_homepage_no_categories_found(self, mock_get_event):
        mock_get_event.return_value = None
        response = self.client.get('/event/0/', {})
        self.assertTemplateUsed(response, 'events/no_event_found.html')

    @patch('events.data.Event.get_events')
    def test_homepage_no_categories_found(self, mock_get_events):
        mock_get_events.return_value = None
        response = self.client.get('/results', {})
        self.assertTemplateUsed(response, 'events/no_results.html')