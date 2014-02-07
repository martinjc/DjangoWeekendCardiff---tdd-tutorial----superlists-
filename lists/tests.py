from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.
class SmokeTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.decode().startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', response.content.decode())
        self.assertTrue(response.content.decode().endswith('</html>'))