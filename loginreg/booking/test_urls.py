"""
from django.urls import reverse
from urllib import response, request
from django.test import TestCase, Client
from .models import Subject, Booking, Request
from django.contrib.auth.models import User

class testUrlsWeb(TestCase):

    def setUp(self):

        username = User.objects.create(username= 'Woraphat', password= 'www12345')
        user1 = User.objects.create(first_name = "Woraphat", last_name = "Wannaphong")
        courseNum1 = Subject.objects.create(class_number = "AAAAA", subject_name="A", section = "000000", semester = "1", Year = "2022", capacity=1)
        #courseNum2 = Subject.objects.create(class_number = "BBBBB", subject_name="B", section = "000000", semester = "1", Year = "2022", capacity=0)

        Booking.objects.create(user=user1, course_number=courseNum1)
        Request.objects.create(username=username)

    def test_regist(self):
        sub = Subject.objects.first()
        b = Booking.objects.first()
        c = Client()

        response = c.post(reverse)
"""

