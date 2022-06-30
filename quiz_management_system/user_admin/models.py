from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models



class UserManager(BaseUserManager):
    def create_user(self, f_name, l_name, email, user_type=None, password=None, is_admin=False, is_staff=True, is_superuser=False, is_active=True):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a Password")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.f_name = f_name
        user_obj.l_name = l_name
        user_obj.user_type = user_type
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_superuser
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, f_name, l_name, email, password=None ):
        user = self.create_user(
            f_name = f_name,
            l_name = l_name,
            email = email,
            password=password,
            is_staff=True,
            is_active=False
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,
            is_superuser=True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    f_name = models.CharField(max_length=60)
    l_name = models.CharField(max_length=60)
    user_type = models.CharField(max_length=60, default='student')
    phone = models.CharField(max_length=60, null=True, blank=True)
    img = models.ImageField(upload_to='user', default='', null=True, blank=True)
    password = models.CharField(max_length=90)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    email_confirmed = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    @property
    def get_fullname(self):
        return self.fast_name + " " + self.last_name





class Common(models.Model):
    active = models.BooleanField(default=False)
    create_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)


class UserProfile(Common):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
