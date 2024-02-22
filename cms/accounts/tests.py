from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

class SignUpAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_signup(self):
        data = {
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890',
            'address': '123 Main St',
            'city': 'Anytown',
            'state': 'AnyState',
            'country': 'US',
            'pincode': '123456'
        }
        response = self.client.post('/signup/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_signup(self):
        # Testing signup with missing required fields
        data = {
            'email': 'test@example.com',
            'password': 'password123'
        }
        response = self.client.post('/signup/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class LoginAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_login(self):
        user = User.objects.create_user(username='testuser', password='password123')
        data = {'email': 'testuser@example.com', 'password': 'password123'}
        response = self.client.post('/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)