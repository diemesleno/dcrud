from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from user.models import User



class IndexView(LoginRequiredMixin, ListView):
    '''
    ClassBaseView to show all users created
    Start Page for logged users
    '''
    model = User
    template_name = 'user/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
