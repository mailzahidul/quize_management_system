from django.db import models
from django.contrib.auth.models import User, Group, AbstractUser
# Create your models here.

class Common(models.Model):
    active = models.BooleanField(default=False)
    create_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)


class UserProfile(Common):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
