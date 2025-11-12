from django.test import TestCase


class MainAppTests(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
