from ast import Sub
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Booking


from .models import Booking, Subject
# Create your views here.

def index(request):
    # who
    user = User.objects.get(pk=request.user.id)

    # enrolled subject
    enrolled_subjects = Booking.objects.filter(user=user)

    id = []
    for subject in enrolled_subjects:
        id.append(subject.course_number.id)
    subjects = Subject.objects.exclude(pk__in=id)

    return render(request, "booking/index.html",{
        'subjects': subjects
    })

def bookings(request, subject_id):
    user = User.objects.get(pk=request.user.id)
    subject = Subject.objects.get(id=subject_id)

    check = Booking.objects.filter(user=user, course_number=subject).first()

    if check is None:
        booking = Booking.objects.create(user=user, course_number=subject)

        subjects = Booking.objects.filter(user=user)
        return render(request,'booking/booking.html', {
            'subjects': subjects,
        })

def checksubreg(request):
    user = User.objects.get(pk=request.user.id)
    enrolled_subjects = Booking.objects.filter(user=user)

    return render(request,'booking/booking.html', {
        'subjects': enrolled_subjects,
    })

def withdraw(request, subject_id):
    user = User.objects.get(pk=request.user.id)
    subject = Subject.objects.get(id=subject_id)

    check = Booking.objects.filter(user=user, course_number=subject).first()

    if check is not None:
        # withdraw = Booking.objects.delete(user=user, course_number=subject)
        check.delete()

        subjects = Booking.objects.filter(user=user).all()
        print(subjects)
        return HttpResponseRedirect(reverse('booking:index')) 