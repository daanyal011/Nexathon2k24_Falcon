from django.contrib import admin
from .models import Classroom, Student, Attendance,Teacher

admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Attendance)
