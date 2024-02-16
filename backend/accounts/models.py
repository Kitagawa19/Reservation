from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractUser,
    Group,
)
# Create your models here.

class CustomUser(AbstractUser):
  def _create_user(self,username,password=None,**extra_fields):
    if not username:
      raise ValueError('The username must be set')
    user = self.model(username=username,**extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

class CustomUserManager(BaseUserManager):
  def create_user(self,username,password=None,**extra_fields):
    extra_fields.setdefault('is_staff',True)
    extra_fields.setdefault('is_superuser',False)
    user = self._create_user(username,password,**extra_fields)
    is_student , created = Group.objects.get_or_create(name='student')
    user.groups.add(is_student)
    return  user

  def create_superuser(self,username,password=None,**extra_fields):
    extra_fields.setdefault('is_staff',True)
    extra_fields.setdefault('is_superuser',True)
    user = self._create_user(username,password,**extra_fields)
    is_superuser , created = Group.objects.get_or_create(name='superuser')
    user.groups.add(is_superuser)
    return user