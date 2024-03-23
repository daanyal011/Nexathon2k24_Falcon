from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Classroom, Attendance
from .forms import QRScanForm, MarkAttendanceForm

@login_required
def scan_qr(request):
    if request.method == 'POST':
        form = QRScanForm(request.POST)
        if form.is_valid():
            qr_code = form.cleaned_data['qr_code']
            try:
                classroom = Classroom.objects.get(qr_code=qr_code)
                request.session['classroom_id'] = classroom.id
                return redirect('mark_attendance')
            except Classroom.DoesNotExist:
                messages.error(request, 'Invalid QR code')
    else:
        form = QRScanForm()
    return render(request, 'attendance/scan_qr.html', {'form': form})

@login_required
def mark_attendance(request):
    classroom_id = request.session.get('classroom_id')
    classroom = Classroom.objects.get(id=classroom_id)
    students = Student.objects.filter(classroom=classroom)
    if request.method == 'POST':
        form = MarkAttendanceForm(request.POST)
        if form.is_valid():
            student_ids = form.cleaned_data['student_ids']
            for student_id in student_ids:
                student = Student.objects.get(id=student_id)
                Attendance.objects.create(student=student, classroom=classroom)
            messages.success(request, 'Attendance marked successfully')
            return redirect('scan_qr')
    else:
        form = MarkAttendanceForm()
    return render(request, 'attendance/mark_attendance.html', {'form': form, 'classroom': classroom, 'students': students})
