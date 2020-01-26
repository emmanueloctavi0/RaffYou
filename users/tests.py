from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate


class UsersTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email='test@gmail.com',
            username='test_user',
            password='secret@123',
            first_name='User first name',
            last_name='User last name'
        )

    def test_user_login_with_email(self):
        """A user can log in the website with their email"""
        user = authenticate(username='test@gmail.com', password='secret@123')
        self.assertEqual(user, self.user)
        self.assertEqual(user.email, self.user.email)
