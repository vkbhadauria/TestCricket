from django.test import TestCase
from match.api.views import TeamViewSet
from django.test.client import RequestFactory


class TestTeamAPI(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()

    def test_teamList(self):
        self.request = self.request_factory.get('/')
        response = TeamViewSet.as_view()(self.request)
        print(response)
        self.assertEqual(response.status_code, 200)
