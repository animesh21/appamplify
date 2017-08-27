from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import AWSInstanceModel, AWSCredentialsModel, AWSSpotInstanceRequestModel


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'id': 'user_email',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'user_password',
            'placeholder': 'Password'
        })
    )


class AddInstanceForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password'
        })
    )

    class Meta:
        model = AWSInstanceModel
        fields = ['name', 'login_name', 'ip_address',
                  'port_number', 'key', 'password']


class AddCredentialsForm(forms.ModelForm):
    class Meta:
        model = AWSCredentialsModel
        fields = ['access_key', 'secret_key']


class AWSSpotInstanceRequestForm(forms.ModelForm):

    class Meta:
        model = AWSSpotInstanceRequestModel
        fields = ['num_instances', 'instance_type', 'max_price', 'expiration_time']


class AWSSpotInstanceMonitorForm(forms.Form):
    request_id = forms.CharField(max_length=128)
