from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from teamwork_app.models import Employee


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(
        label="Имя", widget=forms.TextInput(attrs={"class": "form-group", "placeholder": "Имя"})
    )
    second_name = forms.CharField(
        label="Фамилия", widget=forms.TextInput(attrs={"class": "form-group", "placeholder": "Фамилия"})
    )
    fam_name = forms.CharField(
        label="Отчество", widget=forms.TextInput(attrs={"class": "form-group", "placeholder": "Отчество"})
    )
    email = forms.CharField(
        label="Email", widget=forms.EmailInput(attrs={"class": "form-group", "placeholder": "Email"})
    )
    password1 = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-group", "placeholder": "Пароль"})
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={"class": "form-group", "placeholder": "Подтверждение пароля"}),
    )

    class Meta:
        model = Employee
        fields = ("first_name", "second_name", "fam_name", "email", "password1", "password2", "is_manager", "post")


class LoginUserForm(AuthenticationForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-group"}))
