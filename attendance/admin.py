from django.contrib import admin
from .models import Subject, Classroom, Student, Teacher, Attendance

# Register your models here.
admin.site.register(Subject)
admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Attendance)