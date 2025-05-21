from django import forms
from django.contrib.auth.models import User
from . import models
from django.forms import modelformset_factory
from .models import Qualification, Subject, Achievement

class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model=models.Teacher
        fields=['address','mobile','profile_pic']



QualificationFormSet = modelformset_factory(Qualification, fields=('degree', 'institution', 'year_of_passing'), extra=1)
SubjectFormSet = modelformset_factory(Subject, fields=('name',), extra=1)
AchievementFormSet = modelformset_factory(Achievement, fields=('title', 'description', 'date'), extra=1)

