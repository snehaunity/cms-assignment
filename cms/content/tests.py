from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import ContentItem


class ContentAPITestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Create some content items for testing
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_content_item(self):
        data = {
            'title': 'Test Title',
            'body': 'Test Body',
            'summary': 'Test Summary',
            'categories': ['Category1', 'Category2']
        }
        response = self.client.post('/content/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_content_item(self):
        content_item = ContentItem.objects.create(title='Test Title', body='Test Body', summary='Test Summary')
        response = self.client.get(f'/content/{content_item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_content_item(self):
        content_item = ContentItem.objects.create(title='Test Title', body='Test Body', summary='Test Summary')
        data = {
            'title': 'Updated Title',
            'body': 'Updated Body',
            'summary': 'Updated Summary'
        }
        response = self.client.put(f'/content/{content_item.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_content_item(self):
        content_item = ContentItem.objects.create(title='Test Title', body='Test Body', summary='Test Summary')
        response = self.client.delete(f'/content/{content_item.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

