from unittest import TestCase
from django.test import Client
from .response import INSUFFICIENT_INFORMATION, INVALID_CREDENTIALS

class LoginManagerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_insufficient_information(self):
        # Neither an email address or password provided
        response = self.client.post('/api/users/login/', {})
        self.assertEqual(response.status_code, INSUFFICIENT_INFORMATION.status_code)

        # No email address provided
        response = self.client.post('/api/users/login/', {'password': 'testpassword'})
        self.assertEqual(response.status_code, INSUFFICIENT_INFORMATION.status_code)

        # No password provided
        response = self.client.post('/api/users/login/', {'email': 'jdoe@example.org'})
        self.assertEqual(response.status_code, INSUFFICIENT_INFORMATION.status_code)

    def test_invalid_credentials(self):
        # Invalid email address and password
        response = self.client.post('/api/users/login/', {'email': 'invalid@email.com', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, INVALID_CREDENTIALS.status_code)

        # Invalid email address
        response = self.client.post('/api/users/login/', {'email': 'invalid@email.com', 'password': 'testpassword'})
        self.assertEqual(response.status_code, INVALID_CREDENTIALS.status_code)

        # Invalid password
        response = self.client.post('/api/users/login/', {'email': 'jdoe@example.org', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, INVALID_CREDENTIALS.status_code)
