from django.db import models

from student.models import Student

QUALIFICATION_CHOICES = [
    ('10th', '10th Standard'),
    ('11th', '11th Standard'),
    ('12th', '12th Standard'),
    ('bsc_1st_year', 'B.Sc. - 1st Year'),
    ('bsc_2nd_year', 'B.Sc. - 2nd Year'),
    ('bsc_3rd_year', 'B.Sc. - 3rd Year'),
    ('bca_1st_year', 'BCA - 1st Year'),
    ('bca_2nd_year', 'BCA - 2nd Year'),
    ('bca_3rd_year', 'BCA - 3rd Year'),
    ('bcom_1st_year', 'B.Com. - 1st Year'),
    ('bcom_2nd_year', 'B.Com. - 2nd Year'),
    ('bcom_3rd_year', 'B.Com. - 3rd Year'),
    ('ba_1st_year', 'B.A. - 1st Year'),
    ('ba_2nd_year', 'B.A. - 2nd Year'),
    ('ba_3rd_year', 'B.A. - 3rd Year'),
    ('mba', 'MBA'),
    ('mca', 'MCA'),
    ('msc', 'M.Sc.'),
    ('ma', 'M.A.'),
    ('mcom', 'M.Com.'),
    ('diploma', 'Diploma'),
    ('phd', 'Ph.D.'),
    ('other', 'Other'),
]
class Course(models.Model):
   course_name = models.CharField(max_length=50)
   qualification = models.CharField(max_length=20, choices=QUALIFICATION_CHOICES,null=True)

   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()

   start_time = models.DateTimeField(null=True, blank=True)
   end_time = models.DateTimeField(null=True, blank=True)
   negative_marking = models.BooleanField(default=False)

   test_duration = models.PositiveIntegerField(default=30, help_text="Test duration in minutes")
   negative_marking_percentage = models.PositiveIntegerField(default=50, help_text="Negative marking in percentage")

   def __str__(self):
        return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

