from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.forms import ModelForm

from teamwork_app.models import Employee, Task, Project


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ("first_name", "second_name", "fam_name", "email", "password1", "password2", "is_manager", "post")

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == "is_manager":
                field.widget.attrs.update({"class": "form-check-input", "placeholder": field.label})
            else:
                field.widget.attrs.update({"class": "form-control", "placeholder": field.label})


class LoginUserForm(AuthenticationForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-group"}))

    class Meta:
        model = Employee
        fields = ("email", "password")

    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control", "placeholder": field.label})


class CreateTaskForm(ModelForm):
    description = forms.CharField(
        label="Описание", widget=forms.Textarea()
    )

    class Meta:
        model = Task
        fields = [
            'name',
            'deadline',
            'priority',
            'category',
            'executor',
            'status',
            'project',
            'description'
        ]

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

    def __init__(self, *args, **kwargs):
        super(CreateProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control", "placeholder": field.label})
