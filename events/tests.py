from django.test import TestCase, Client
import unittest

from mock import patch, MagicMock
from data import Event, Category


class TestEventbriteCalled(unittest.TestCase):
    """
    Tests to make sure the right Data function is called for each view
    """

    def setUp(self):
        self.client = Client()

    @patch('events.data.Category.all')
    def test_homepage(self, mock_all):
        mock_all.return_value = MagicMock()
        self.client.get('/', {})
        mock_all.assert_called_once_with()

    @patch('events.data.Event.get_multiple')
    def test_search(self, mock_get_multiple):
        mock_get_multiple.return_value = MagicMock(status_code=200)
        category_ids = [2, 4, 5]

        self.client.get('/results',
                        {"category1": category_ids[0], "category2": category_ids[1], "category3": category_ids[2]})

        mock_get_multiple.assert_called_once_with(category_ids, 1)

    @patch('events.data.Event.get_multiple')
    def test_pagination(self, mock_get_multiple):
        for page_number in range(1, 4):
            mock_get_multiple.return_value = MagicMock(status_code=200)
            category_ids = [2, 4, 5]
            self.client.get('/results/' + str(page_number) + '/',
                            {"category1": category_ids[0], "category2": category_ids[1], "category3": category_ids[2]})

            mock_get_multiple.assert_called_with(category_ids, page_number)

    @patch('events.data.Event.get')
    def test_view_get_event(self, mock_get):
        mock_get.return_value = MagicMock()

        self.client.get('/event/32/', {})
        mock_get.assert_called_once_with('32')


class TestDataFails(unittest.TestCase):
    """
    Tests to check if the Eventbrite API errors, that we return None
    """

    @patch('eventbrite.Eventbrite.get_event')
    def test_get_event_error(self, mock_get_event):
        mock_get_event.return_value = MagicMock(status_code=500)
        event = Event().get(1)
        assert (event is None)

    @patch('eventbrite.Eventbrite.get_categories')
    def test_get_categories_error(self, get_categories):
        get_categories.return_value = MagicMock(status_code=500)
        categories = Category().all()
        assert (categories is None)

    @patch('eventbrite.Eventbrite.get_category')
    def test_get_category_error(self, mock_get_category):
        mock_get_category.return_value = MagicMock(status_code=500)
        category = Category().get(2)
        print category
        assert (category is None)

    @patch('eventbrite.Eventbrite.event_search')
    def test_event_search_error(self, mock_event_search):
        mock_event_search.return_value = MagicMock(status_code=500)
        event = Event().get_multiple([], 1)
        assert (event is None)


class TestDataContracts(unittest.TestCase):
    """
    Tests the linking between our data class and eventbrite API
    """

    @patch('eventbrite.Eventbrite.get_category')
    def test_contract_get_category(self, mock_get_category):
        mock_get_category.return_value = MagicMock(status_code=200)
        Category().get(1)
        mock_get_category.assert_called_once_with(1)

    @patch('eventbrite.Eventbrite.get_categories')
    def test_contract_get_categories(self, mock_get_categories):
        mock_get_categories.return_value = MagicMock(status_code=200)
        Category().all()
        mock_get_categories.assert_called_once_with()

    @patch('eventbrite.Eventbrite.get_event')
    def test_contract_get_event(self, mock_get_event):
        mock_get_event.return_value = MagicMock(status_code=200)
        Event().get(2)
        mock_get_event.assert_called_once_with(2)

    @patch('events.data.Category.get')
    def test_contract_get_categories_two(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200)
        category_ids = [1,2,3]
        Category().get_multiple(category_ids)
        mock_get.assert_called_with(category_ids[2])

    @patch('eventbrite.Eventbrite.event_search')
    def test_contract_event_search(self, mock_event_search):
        mock_event_search.return_value = MagicMock(status_code=200)

        for page_number in range(1, 4):
            mock_event_search.return_value = MagicMock(status_code=200)
            Event().get_multiple([], page_number)

            mock_event_search.assert_called_with(**{"page": page_number, "categories": []})


class TestViews(TestCase):
    """
    Tests that check that an error message is displayed if we have nothing returned
    """

    @patch('events.data.Category.all')
    def test_no_categories_found(self, mock_all):
        mock_all.return_value = None
        response = self.client.get('/', {})
        self.assertTemplateUsed(response, 'events/no_categories_found.html')

    @patch('events.data.Event.get')
    def test_no_event_found(self, mock_get):
        mock_get.return_value = None
        response = self.client.get('/event/0/', {})
        self.assertTemplateUsed(response, 'events/no_event_found.html')

    @patch('events.data.Event.get_multiple')
    def test_no_events_found(self, mock_get_multiple):
        mock_get_multiple.return_value = None
        response = self.client.get('/results/1/', {})
        self.assertTemplateUsed(response, 'events/no_results.html')
