import qrcode
from django.shortcuts import render, redirect
from django.contrib import messages
from attendance.models import Classroom, Student, Attendance
from django.http import HttpResponse

def generate_qr(request):
    if request.method == 'POST':
        classroom_id = request.POST.get('classroom_id')
        try:
            classroom = Classroom.objects.get(pk=classroom_id)
            qr_data = f"Classroom: {classroom.name}\nQR Code: {classroom.qr_code}"
            qr = qrcode.make(qr_data)
            response = HttpResponse(content_type='image/png')
            qr.save(response, 'PNG')
            return response
        except Classroom.DoesNotExist:
            messages.error(request, 'Invalid classroom ID')
            return redirect('generate_qr')
    return render(request, 'attendance/generate_qr.html')


from django.shortcuts import redirect
from django.contrib import messages
from .models import Classroom, Student, Attendance

def mark_attendance(request):
    if request.method == 'POST':
        qr_code = request.POST.get('qr_code')
        try:
            classroom = Classroom.objects.get(qr_code=qr_code)
            if request.user.is_authenticated:
                student = Student.objects.get(user=request.user)
                Attendance.objects.create(student=student, classroom=classroom)
                messages.success(request, 'Attendance marked successfully')
                return redirect('attendance_success')
            else:
                messages.error(request, 'You must be logged in as a student to mark attendance.')
        except Classroom.DoesNotExist:
            messages.error(request, 'Invalid QR code')
    return redirect('home')  # Redirect to home or login page

def scan_qr(request):
    if request.method == 'POST':
        qr_code = request.POST.get('qr_code')
        try:
            classroom = Classroom.objects.get(qr_code=qr_code)
            if request.user.is_authenticated:
                student = Student.objects.get(user=request.user)
                Attendance.objects.create(student=student, classroom=classroom)
                messages.success(request, 'Attendance marked successfully')
                return redirect('attendance_success')
            else:
                messages.error(request, 'You must be logged in as a student to mark attendance.')
        except Classroom.DoesNotExist:
            messages.error(request, 'Invalid QR code')
    return render(request, 'attendance/scan_qr.html')