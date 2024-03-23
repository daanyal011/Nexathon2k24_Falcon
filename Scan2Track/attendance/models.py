from django.db import models

from users.models import UserProfile

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    qr_code = models.CharField(max_length=100, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    geofence_radius = models.FloatField()

    def __str__(self):
        return self.name

class Student(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    attendance_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.classroom.name}"
