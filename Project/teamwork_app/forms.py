from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginUserForm(AuthenticationForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-group"}))
