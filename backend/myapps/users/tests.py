from django.test import TestCase
from myapps.users.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class ProductTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.user = User(username="a@a.com", name="User Test", surname="Test")
        self.user.save()

    def tearDown(self):
        super().tearDown()
        self.user = None

    def test_store_product(self):
        self.assertEqual(User.objects.count(), 1)

    def test_user_created(self):
        user = User.objects.all()[0]
        self.assertEqual(user.username, "a@a.com")
        self.assertEqual(user.name, "User Test")
        self.assertEqual(user.surname, "Test")
