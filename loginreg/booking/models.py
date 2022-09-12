from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    class_number = models.CharField(max_length=5, default="")
    subject_name = models.CharField(max_length=64, default="")
    section = models.CharField(max_length=10, default="")
     
    def __str__(self):
        return f"{self.class_number} {self.subject_name} {self.section}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    course_number = models.ForeignKey(Subject, on_delete=models.CASCADE, default="")
    
    def __str__(self):
        return f"{self.user} {self.course_number}"