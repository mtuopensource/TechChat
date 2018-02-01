from unittest import TestCase
from django.test import Client
from .response import INSUFFICIENT_INFORMATION, INVALID_CREDENTIALS

class LoginManagerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_insufficient_information(self):
        response = self.client.post('/api/users/login/', {}) # Neither an email address or password
        self.assertEqual(response.status_code, INSUFFICIENT_INFORMATION.status_code)

        response = self.client.post('/api/users/login/', {'password': 'testpassword'}) # No email address provided
        self.assertEqual(response.status_code, INSUFFICIENT_INFORMATION.status_code)

        response = self.client.post('/api/users/login/', {'email': 'jdoe@example.org'}) # No password provided
        self.assertEqual(response.status_code, INSUFFICIENT_INFORMATION.status_code)

    def test_invalid_credentials(self):
        response = self.client.post('/api/users/login/', {'email': 'invalid@email.com', 'password': 'invalidpassword'}) # Invalid email address and password
        self.assertEqual(response.status_code, INVALID_CREDENTIALS.status_code)

        response = self.client.post('/api/users/login/', {'email': 'invalid@email.com', 'password': 'testpassword'}) # Invalid email address
        self.assertEqual(response.status_code, INVALID_CREDENTIALS.status_code)

        response = self.client.post('/api/users/login/', {'email': 'jdoe@example.org', 'password': 'invalidpassword'}) # Invalid password
        self.assertEqual(response.status_code, INVALID_CREDENTIALS.status_code)
