from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
import uuid

# Create your models here.


class UsersManager(BaseUserManager):

    def create_user(self, email, user_name, password, **others):
        if not email:
            raise ValueError("Email invalido")
        email = self.normalize_email(email)
        user = self.model(email=email, username=user_name,**others)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **others):

        others.setdefault('is_staff', True)
        others.setdefault('is_active', True)
        others.setdefault('is_superuser', True)

        return self.create_user(email,username, password, **others)


class Users(AbstractUser, PermissionsMixin):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(unique=True, blank=False)
    username = models.CharField(max_length=60, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField(blank=False, null=True)
    join_date = models.DateField(default=timezone.now)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UsersManager()

    def __str__(self):
        return f'username= {self.username}, email= {self.email}, is_active={self.is_active} , is_staff={self.is_staff}'
