from django.urls import path, include
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/<int:subject_id>', views.bookings, name='booking'),
    path('checksubreg/', views.checksubreg, name= 'checksubreg'),

]