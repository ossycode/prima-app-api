"""
Tests for the user API.
"""
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import  reverse


from rest_framework.test import APIClient
from rest_framework import status



CREATE_USER_URL = reverse('users:users')

def create_user(**params):
    """Create and return a new user"""
    return get_user_model().objects.create_user(**params)

class PostUserApiTests(TestCase):
    """Test the public features of the user API."""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating a user is successful."""
        payload = {
            'email': 'test6@example.com',
            'username': 'testUser8',
            'password': 'testpass123',
            'name': 'Test Name'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_with_email_username_exists_error(self):
        """Test error returned if user with email or username exisit"""
        payload =  {
            'email': 'test@example.com',
            'username': 'testUser7',
            'password': 'testpass123',
            'name': 'Test Name'
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test an error is returned if password less than 5 chars"""
        payload =  {
            'email': 'test@example.com',
            'username': 'testUser',
            'password': 'test',
            'name': 'Test Name'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)

class GetSingleUserApiTests(TestCase):
    """Test API requests for retriving single user."""
    def setUp(self):
        self.user = create_user(
            email='test@example.com',
            username='testUser2',
            password='testpass123',
            name='Test Name'
        )
        self.client = APIClient()
        self.manage_user_url = reverse('users:user-detail', args=[self.user.id])

    def test_retrive_user_success(self):
        """Test retriving a single data by Id"""
        res = self.client.get(self.manage_user_url )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'id': self.user.id,
            'name': self.user.name,
            'email': self.user.email,
            'username': self.user.username,
        })
    
    def test_post_userid_not_allowed(self):
        """Test POST is not allowed for the user_id endpoint"""
        res = self.client.post(self.manage_user_url , {})

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
