from django.db import models

# Create your models here.

class Common(models.Model):
    active = models.BooleanField(default=True)

class Subject(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Quiz(Common):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.CharField(max_length=250, null=True)
    option_1 = models.CharField(max_length=100, null=True)
    option_2 = models.CharField(max_length=100, null=True)
    option_3 = models.CharField(max_length=100, null=True)
    option_4 = models.CharField(max_length=100, null=True)
    answer = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.question