from django.db import models
from user_admin.models import UserProfile
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Semester(models.Model):
    semester_name = models.CharField(max_length=150)
    semester_year = models.CharField(max_length=150)
    create_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.semester_name

class Course(models.Model):
    course_name = models.CharField(max_length=150)
    course_description = models.CharField(max_length=150)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester_name = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    create_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name


class Quiz(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    marks = models.IntegerField(default=1)
    answer = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.question


class Result(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.IntegerField()
    exam_date = models.DateField(auto_now_add=True)
    comments = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.question