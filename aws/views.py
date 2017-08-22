from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views.generic import FormView, CreateView, RedirectView
from django.urls import reverse
from .forms import LoginForm
from django.contrib.auth.models import User
from .forms import AddInstanceForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'aws/signup.html'
    model = User

    def get_success_url(self):
        return reverse('login')


class UserLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'aws/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('dashboard')


class DashboardView(LoginRequiredMixin, FormView):
    template_name = 'aws/dashboard.html'
    form_class = AddInstanceForm


class UserLogoutView(LogoutView):
    def get_next_page(self):
        return reverse('login')

class NotFoundView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('login')
