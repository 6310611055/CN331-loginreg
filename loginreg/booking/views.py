from ast import Sub
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User


from .models import Booking, Subject
# Create your views here.

def index(request):
    subject = Subject.objects.all()
    return render(request, "booking/index.html",{
        'subject': subject
    })

def bookings(request, subject_id):
    try:
        user = User.objects.get(pk=request.user.id)
        subject = Subject.objects.get(id=subject_id)
        booking = Booking.objects.create(user=user, course_number=subject)
        return render(request,'booking/booking.html', {
            'bookings': bookings,
        })
    except Exception as e:
        print("Error on booking : ", e)
    return index(request)
        

def book(request, booking_user):
    pass

    
    


#def index(request):
#   return render(request, "subject/index.html",{
#       'subject': Subject.objects.all()
#   })

