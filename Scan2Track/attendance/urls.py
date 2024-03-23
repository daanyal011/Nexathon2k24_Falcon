from django.urls import path
from . import views

urlpatterns = [
    path('generate_qr/', views.generate_qr, name='generate_qr'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
]
