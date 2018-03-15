from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from localflavor.generic.models import IBANField
from django.conf import settings
from django.db.models.signals import pre_save

import uuid

class User(AbstractUser):
    '''
    The user extend AbstractUser and I added 2 new fields
    '''
    iban = IBANField(unique=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    email = models.EmailField('E-mail', unique=True)
    username = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        '''
        Just to not return a object without information
        '''
        return self.first_name


'''
Using signal against override save method
'''
def user_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.creator:
        instance.is_superuser = True
        instance.is_staff = True
        instance.username = instance.email
        instance.iban = str(uuid.uuid4())
        instance.set_password(instance.email)
    else:
        instance.is_superuser = False
        instance.username = str(uuid.uuid4())
        instance.email = str(uuid.uuid4())

pre_save.connect(user_pre_save_receiver, sender=User)
