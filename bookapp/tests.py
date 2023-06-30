from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class HomePageTest(TestCase):
    def test_url_exists_at_location(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("book_list_api_view"))
        self.assertEqual(response.status_code, 200)

    def test_template_content(self):
        response = self.client.get(reverse("book_list_api_view"))
        self.assertNotContains(response, "Not on the page")
