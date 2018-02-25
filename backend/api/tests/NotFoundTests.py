from django.test import Client
from unittest import TestCase
from api.response import NOT_FOUND

class NotFoundTests(TestCase):
    # Login
    def setUp(self):
        self.client = Client()
        self.client.post('/api/users/login/', {'email': 'test@mtu.edu', 'password': 'test'})

    # Provides an invalid Board id and expects an HTTP_404_NOT_FOUND response.
    def test_invalid_id_board(self):
        response = self.client.get('/api/boards/badid/')
        self.assertEqual(response.status_code, NOT_FOUND.status_code)

    # Provides an invalid Posts id and expects an HTTP_404_NOT_FOUND response.
    def test_invalid_id_thread(self):
        response = self.client.get('/api/threads/badid/')
        self.assertEqual(response.status_code, NOT_FOUND.status_code)
