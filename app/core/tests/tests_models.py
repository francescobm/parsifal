from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Test creating a new user with emaol"""
        email = 'test.fra@bobby.com'
        password = 'foffy'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'myemail@UPPERCASE.COM'
        user = get_user_model().objects.create_user(email=email, password='whatever')

        self.assertEqual(user.email, email.lower())

    def test_new_user_missing_email(self):
        """Test creating user with no email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'whatever')
    
    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser('myemai@email.com', 'hello123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


