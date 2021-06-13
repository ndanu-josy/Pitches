
import unittest
from app.models import User
from os import urandom

class UserModelTest(unittest.TestCase):
    """
    Test class to test the behaviour of the user class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """

        self.new_user = User(username='ndanu', password = '1234')


    def test_password(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_passwordAccess(self):
        with self.assertRaises(AttributeError):
            self.new_user.password


    def test_verifyPassword(self):
        self.assertTrue(self.new_user.verify_password('1234'))



    def tearDown(self):
        user = User.query.filter_by(username="ndanu").first()
        if user:
            print("found")