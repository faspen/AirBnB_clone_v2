#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):

    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value(first_name="Finn")
        self.assertEqual(type(new.first_name), str)
        self.assertEqual(new.first_name, "Finn")

    def test_last_name(self):
        """ """
        new = self.value(last_name="Aspenson")
        self.assertEqual(type(new.last_name), str)
        self.assertEqual(new.last_name, "Aspenson")

    def test_email(self):
        """ """
        new = self.value(email="hello@whatever.com")
        self.assertEqual(type(new.email), str)
        self.assertEqual(new.email, "hello@whatever.com")

    def test_password(self):
        """ """
        new = self.value(password="passwordlol")
        self.assertEqual(type(new.password), str)
        self.assertEqual(new.password, "passwordlol")
