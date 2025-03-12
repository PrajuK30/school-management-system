# school/tests.py
from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def test_create_user(self):
        # Create a User instance
        user = User.objects.create(
            name="John Doe", 
            email="john.doe@example.com", 
            password="password123", 
            role="student"
        )
        
        # Assert the name of the user is correctly saved
        self.assertEqual(user.name, "John Doe")
        
        # Assert the email is correctly saved
        self.assertEqual(user.email, "john.doe@example.com")
        
        # Assert the role is correctly set as 'student'
        self.assertEqual(user.role, "student")
        
        # Ensure that the password field is stored correctly (hashed in the database)
        self.assertNotEqual(user.password, "password123")  # Password should be hashed, not plain text
