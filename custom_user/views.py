from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from . import forms


# Create your views here.


class RegisterView(CreateView):
    form_class = forms.CustomRegisterForm
    template_name = 'users/register.html'
    success_url = '/login/'


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('users:persons')


class UsersListView(ListView):
    model = User
    template_name = 'users/users_list.html'

    def get_queryset(self):
        return self.model.objects.all()


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')
