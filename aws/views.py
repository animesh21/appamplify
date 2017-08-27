from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import FormView, CreateView, RedirectView
from django.urls import reverse
from django.shortcuts import redirect
from .forms import LoginForm, AddCredentialsForm, AWSSpotInstanceRequestForm
from .forms import AWSSpotInstanceMonitorForm
from .models import AWSCredentialsModel, AWSSpotInstanceRequestModel


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
    form_class = AddCredentialsForm

    def get(self, request, *args, **kwargs):
        user = self.request.user
        aws_credentials = AWSCredentialsModel.objects.filter(
            user=user
        ).first()
        if aws_credentials:
            aws_credentials.configure()
            return redirect(self.get_success_url())
        return super().get(self, request, *args, **kwargs)

    def form_valid(self, form):
        access_key = form.cleaned_data['access_key']
        secret_key = form.cleaned_data['secret_key']
        user = self.request.user
        aws_credentials = AWSCredentialsModel.objects.get_or_create(
            user=user)[0]
        aws_credentials.access_key = access_key
        aws_credentials.secret_key = secret_key
        aws_credentials.save()
        messages.add_message(self.request, messages.INFO,
                             'Credentials saved successfully, id: ' +
                             str(aws_credentials.id))
        aws_credentials.configure()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('configuration')


class ConfigurationView(LoginRequiredMixin, FormView):
    form_class = AWSSpotInstanceRequestForm
    template_name = 'aws/configure.html'

    def get_success_url(self):
        return reverse('monitor')

    def form_valid(self, form):
        user = self.request.user
        num_instances = form.cleaned_data['num_instances']
        instance_type = form.cleaned_data['instance_type']
        max_price = form.cleaned_data['max_price']
        expiration_time = form.cleaned_data['expiration_time']
        # print('Expiration time type: {}'.format(type(expiration_time)))
        spot_instance_request = AWSSpotInstanceRequestModel.objects.create(
            user=user,
            num_instances=num_instances,
            instance_type=instance_type,
            max_price=max_price,
            expiration_time=expiration_time
        )
        spot_instance_request.request_fleet()
        messages.add_message(self.request, messages.INFO, "Request placed successfully")
        return redirect(self.get_success_url())


class RequestMonitorView(LoginRequiredMixin, FormView):
    form_class = AWSSpotInstanceMonitorForm
    template_name = 'aws/monitor.html'

    def get_success_url(self):
        return reverse('monitor')


class UserLogoutView(LogoutView):
    def get_next_page(self):
        return reverse('login')


class NotFoundView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('login')
