from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:bookings_user>', views.bookings, name='bookings')
]