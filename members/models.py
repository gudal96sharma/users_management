from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class User(AbstractBaseUser):
    name            = models.CharField(max_length=25, null=False, blank=False, default=True)
    email           = models.EmailField(max_length=50, null=False, blank=False, unique=True)
    password        = models.CharField(max_length=1024, null=True, blank=True)
    emp_code        = models.CharField(max_length=10, null=True, unique=True)
    state           = models.CharField(max_length=30, null=True)
    city            = models.CharField(max_length=30, null=True)
    is_active       = models.BooleanField(default=True)
    registered_on   = models.DateTimeField(auto_now_add=True,null = True)
    
    USERNAME_FIELD = 'email'

    class Meta:
        managed = True
        db_table = 'users'