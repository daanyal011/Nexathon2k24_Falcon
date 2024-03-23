from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    is_teacher = forms.BooleanField(required=False)  # Added is_teacher field

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_teacher']  # Include is_teacher field in fields list

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['is_teacher']
