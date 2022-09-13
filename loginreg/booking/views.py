from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User


from .models import Booking, Subject
# Create your views here.

def index(request):
    booking = Booking.objects.all()
    return render(request, "booking/index.html",{
        'booking': booking
    })

def bookings(request, bookings_user):
    bookings = Booking.objects.get(pk = bookings_user)
    user = User.objects.all()
    return render(request,'booking/booking.html', {
        'bookings': bookings,
        'students' : user,
    })

def book(reauest, booking_user):
    pass

    
    


#def index(request):
#   return render(request, "subject/index.html",{
#       'subject': Subject.objects.all()
#   })

