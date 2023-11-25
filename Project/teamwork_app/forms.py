from django.conf.global_settings import DATE_INPUT_FORMATS
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.forms import ModelForm

from teamwork_app.models import Employee, Task, Project


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(
        label="Имя", widget=forms.TextInput(attrs={"class": "form-group", "placeholder": "Имя"})
    )
    second_name = forms.CharField(
        label="Фамилия", widget=forms.TextInput(attrs={"class": "form-group", "placeholder": "Фамилия"})
    )
    fam_name = forms.CharField(
        label="Отчество", required=False, widget=forms.TextInput(attrs={"class": "form-group", "placeholder": "Отчество"})
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

    class Meta:
        model = Employee
        fields = ("email", "password")

    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-group", "placeholder": field.label})


class CreateTaskForm(ModelForm):
    description = forms.CharField(
        label="Описание", widget=forms.Textarea()
    )
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'deadline',
            'priority',
            'category',
            'executor',
            'status',
            'project'
        ]
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'deadline': 'Дата окончания',
            'priority': 'Приоритет',
            'category': 'Тип задачи',
            'executor': 'Исполнитель',
            'status': 'Статус задачи',
            'project': 'Проект'
        }

    def __init__(self, *args, **kwargs):
        super(CreateTaskForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control", "placeholder": field.label})


class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'employee',
        ]
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'employee': 'Сотрудники проекта',
        }

    def __init__(self, *args, **kwargs):
        super(CreateProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-group", "placeholder": field.label})
