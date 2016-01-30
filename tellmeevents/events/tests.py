from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class TestViews(TestCase):
    def test_searching_no_input(self):
        client = Client()
        response = client.get(reverse('events_search'), {})

        self.assertEqual(response.status_code, 200)
