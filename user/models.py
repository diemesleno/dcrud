from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.generic.models import IBANField
from django.conf import settings


class User(AbstractUser):
    '''
    The user extend AbstractUser and I added 2 new fields
    '''
    iban = IBANField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        '''
        If the user create account using Google Authentication he will
        no have creator but in this case will be superuser. If the user
        was created by a superuser, so will be a normal user.

        As we don't need username here, I put the email hash as username.
        '''
        if not self.creator:
            self.is_superuser = True
        else:
            self.is_superuser = False
        self.username = hash(self.first_name + '' + self.last_name)
        super().save(*args, **kwargs)

    def __str__(self):
        '''
        Just to not return a object without information
        '''
        return self.first_name

