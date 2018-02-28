from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class UserAdminCreationForm(UserCreationForm):
    '''
    Creating the form to create users. Here we need only 4 fields
    '''
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'iban']
    
    def __init__(self, *args, **kwargs):
        '''
        I'm removing the password because the Administrators will
        login with Google Authentication and the normal users are not
        part of staff.
        '''
        super(UserAdminCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'
    


class UserAdminForm(forms.ModelForm):
    '''
    The admin form will follow the same rule, plus the 2 fields that allow
    enter in the admin area. Not necessary because I remove the option to access
    the admin area.
    '''
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'iban', 'is_active', 'is_staff']
