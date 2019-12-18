from django.test import TestCase
from users.api.views import PlayerViewSet
from django.test.client import RequestFactory


class TestUsersAPI(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()

    def test_playerList(self):
        self.request = self.request_factory.get('/')
        response = PlayerViewSet.as_view()(self.request)
        self.assertEqual(response.status_code, 200)
