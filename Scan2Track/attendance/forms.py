from django import forms
from .models import Classroom, Student

class QRScanForm(forms.Form):
    qr_code = forms.CharField(max_length=100)

class MarkAttendanceForm(forms.Form):
    student_ids = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), widget=forms.CheckboxSelectMultiple)
