from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    # username = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(_('email address'), blank=False)
    tel_number = models.CharField(max_length=20)
    contract_id = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    
    @classmethod
    def get_admin_users(cls):
        return cls.objects.filter(is_staff=True, is_superuser=False)

    @classmethod
    def get_users(cls):
        return cls.objects.filter(is_staff=False, is_superuser=False)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username', ]



