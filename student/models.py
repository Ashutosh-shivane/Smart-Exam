from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/Student/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    qualification = models.CharField(max_length=50, choices=QUALIFICATION_CHOICES, default='10th')

    @property
    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name
