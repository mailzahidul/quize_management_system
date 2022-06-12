from django.db import models

# Create your models here.

class Quiz(models.Model):
    question = models.CharField(max_length=200, null=True)
    option_1 = models.CharField(max_length=200, null=True)
    option_2 = models.CharField(max_length=200, null=True)
    option_3 = models.CharField(max_length=200, null=True)
    option_4 = models.CharField(max_length=200, null=True)
    answer = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question