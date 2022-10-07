from django.urls import reverse
from urllib import response, request
from django.test import TestCase, Client
from .models import Subject, Booking, Request
from django.contrib.auth.models import User
from doctest import REPORT_CDIFF

class LogInOutTest(TestCase):

    def setUp(self):
        user1 = User.objects.create(username= 'Woraphat', password= 'www12345')
        Request.objects.create(username=user1)

    def test_login(self):
        self.client = Client()
        response = self.client.post(reverse('login'), {'username': 'Woraphat', 'password': 'www12345'})
        self.assertEqual(response.status_code, 200)

    def test_login_unsuccessful(self):
        c = Client()
        response = c.post(reverse('login'), {'username': 'Variya', 'password': 'p12345'})
        #self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['message'] == 'Invalid credentials')

        response = c.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        response = c.get(reverse('index'))
        self.assertEqual(response.status_code, 302)


    def test_logout(self):
        self.client = Client()
        response = self.client.post(reverse('logout'))
        self.assertTrue(response.status_code, 302)
