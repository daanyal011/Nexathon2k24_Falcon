from django.db import models

from users.models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
class Classroom(models.Model):
    name = models.CharField(max_length=100)
    qr_code = models.CharField(max_length=100, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    geofence_radius = models.FloatField()

    def __str__(self):
        return self.name
# Define Student and Teacher models
class Student(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    # Add any additional fields for the teacher profile as needed

    def __str__(self):
        return self.user_profile.user.username

# Signal to create Student or Teacher profile based on is_teacher value
@receiver(post_save, sender=UserProfile)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_teacher:
            Teacher.objects.create(user_profile=instance)
        else:
            Student.objects.create(user_profile=instance)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    attendance_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.classroom.name}"
