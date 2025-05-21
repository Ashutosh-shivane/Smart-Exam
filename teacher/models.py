from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/Teacher/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    status= models.BooleanField(default=False)
    salary=models.PositiveIntegerField(null=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name


class Qualification(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='qualifications', on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year_of_passing = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Subject(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='subjects', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='achievements', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title