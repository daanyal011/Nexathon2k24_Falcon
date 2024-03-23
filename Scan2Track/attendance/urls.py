from django.urls import path
from . import views

urlpatterns = [
    path('generate_qr/', views.generate_qr, name='generate_qr'),
    path('scan_qr/', views.scan_qr, name='scan_qr'),
    path('classroom/<int:classroom_id>/attendance/', views.classroom_attendance_list, name='classroom_attendance_list'),
]
