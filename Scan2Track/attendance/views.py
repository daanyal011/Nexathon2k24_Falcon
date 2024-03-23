
# views.py
import qrcode
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Classroom, Student, Attendance
from .forms import QRScanForm, MarkAttendanceForm

# View for generating QR code (accessible by teachers only)
def generate_qr(request):
    # Check if the user is a teacher
    if request.user.is_authenticated and request.user.userprofile.is_teacher:
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
    else:
        # Redirect to home or show error message
        messages.error(request, 'You must be logged in as a teacher to generate QR code.')
        return redirect('home')

# View for scanning QR code and marking attendance (accessible by students)
def scan_qr(request):
    if request.method == 'POST':
        form = QRScanForm(request.POST)
        if form.is_valid():
            qr_code = form.cleaned_data['qr_code']
            try:
                classroom = Classroom.objects.get(qr_code=qr_code)
                if not request.user.is_authenticated or request.user.userprofile.is_teacher:
                    messages.error(request, 'You must be logged in as a student to mark attendance.')
                    return redirect('login')
                student = Student.objects.get(user=request.user)
                Attendance.objects.create(student=student, classroom=classroom)
                messages.success(request, 'Attendance marked successfully')
                return redirect('attendance_success')
            except Classroom.DoesNotExist:
                messages.error(request, 'Invalid QR code')
    else:
        form = QRScanForm()
    return render(request, 'attendance/scan_qr.html', {'form': form})