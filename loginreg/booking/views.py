from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Booking, Student, Subject
# Create your views here.

def index(request):
    booking = Booking.objects.all()
    return render(request, "booking/index.html",{
        'booking': booking
    })

def bookings(request, bookings_user):
    bookings = Booking.objects.get(pk = bookings_user)
    return render(request,'booking/booking.html', {
        'bookings': bookings,
        'student' : bookings.student.all(),
    })

    
    


#def index(request):
#   return render(request, "subject/index.html",{
#       'subject': Subject.objects.all()
#   })

