#!/usr/bin/python3
"""
test case for user
"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """
    class for testing User
    """
    def test_instance_creation(self):
        """
        tests creation
        """
        user = User()
        self.assertIsInstance(user, User)

    def test_attributes(self):
        """
        tests attributes
        """
        user = User()
        user.email = "test@example.com"
        user.password = "secure_password"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "secure_password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

if __name__ == '__main__':
    unittest.main()
