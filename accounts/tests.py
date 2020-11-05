from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {
            "username": "9731174558",
            "email": "acs@gmail.com",
            "password1": "LovrMy52",
            "password2": "LovrMy52",
            "name": "Tousif",
        }
        response = self.client.post("/accounts/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class CreateContact(APITestCase):
#     def setUp(self):
#         user = User.objects.create_user('9731174558', 'LovrMy52')
#         self.client.login(username='9731174558', password='LovrMy52')
#         response = self.client.get(reverse('check_user'))
#         self.assertEqual(response.status_code, httplib.OK)