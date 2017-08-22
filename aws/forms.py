from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import AWSInstanceModel

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
        fields = ['user', 'name', 'login_name', 'ip_address', 'port_number', 'key', 'password']
