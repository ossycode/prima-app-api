"""
Test for models
"""
import os, django
from django.test import TestCase
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpassword12'
        username = 'testuser'

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            username=username
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com', 'testuser1'],
            ['Test2@Example.com', 'Test2@example.com', 'testuser2'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com', 'testuser3'],
            ['test4@example.COM', 'test4@example.com', 'testuser4'],
        ]
        for email, expected_email, username in sample_emails:
            user = get_user_model().objects.create_user(email, username, 'pass123')
            self.assertEqual(user.email, expected_email)

    def test_new_user_without_email_or_username_raises_error(self):
        """Test that creating a user without an email or username raises ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', '', 'test123')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'test1@example.com', 'testuser1','testpassword123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)