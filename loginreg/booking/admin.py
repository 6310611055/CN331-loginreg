from django.contrib import admin

from .models import Booking, Student, Subject

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "course_number")


class SubjectAdmin(admin.ModelAdmin):
    pass

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Booking, BookingAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)