from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.scan_qr, name='scan_qr'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
]
