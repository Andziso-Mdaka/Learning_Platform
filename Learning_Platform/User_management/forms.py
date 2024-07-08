# user_management/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import User

class LoginForm(AuthenticationForm):
    email = forms.EmailField(label=_("Email"), widget=forms.EmailInput)
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')