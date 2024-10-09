"""
Test for models.
"""

from django.test import TestCase

from django.contrib.auth import get_user_model


class UserModelTest(TestCase):
    """Test for User model."""
    email = "test@example.com"
    password = "testpass123"

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password,
        )
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized."""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, self.password)
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", self.password)

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            self.email,
            self.password,
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
