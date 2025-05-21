from django import forms
from django.contrib.auth.models import User
from . import models
from django.forms import Select
from .models import Course

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class TeacherSalaryForm(forms.Form):
    salary=forms.IntegerField()

class CourseForm(forms.ModelForm):
    class Meta:
        model=models.Course
        fields=['course_name','question_number','total_marks', 'negative_marking','test_duration']





class CourseSelectWidget(Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)

        # Dynamically fetch the total question count for the course
        if value:
            try:
                course = Course.objects.get(id=value)
                option['attrs']['data-total-question'] = course.question_set.count()
            except Course.DoesNotExist:
                pass

        return option


class QuestionForm(forms.ModelForm):
    
    #this will show dropdown __str__ method course model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in course model and return it
    # courseID=forms.ModelChoiceField(queryset=models.Course.objects.all(),
    #                                 empty_label="Course Name",
    #                                 to_field_name="id",
    #                                 widget=CourseSelectWidget())
    class Meta:
        model=models.Question
        fields=['marks','question','option1','option2','option3','option4','answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }
        exclude = ['course']


