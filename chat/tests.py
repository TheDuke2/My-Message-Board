from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text='This is the test data for Post')

    def test_model_data(self):
        self.assertEqual(self.post.text, 'This is the test data for Post')

    def test_url_exist_in_correct_location(self):
        response = self.client.get('/chat/')
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse('chat'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'This is the test data for Post')