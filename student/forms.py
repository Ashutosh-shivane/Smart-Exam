from django import forms
from django.contrib.auth.models import User
from . import models
from student.models import Student
from exam import models as QMODEL

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields=['address','mobile','profile_pic']
        widgets = {
            'qualification': forms.Select(choices=Student.QUALIFICATION_CHOICES)
        }

