from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth.password_validation import validate_password

from teamwork_app.forms import LoginUserForm
from teamwork_app.models import POSITION_CHOICES
from teamwork_app.serializers import EmployeeSerializer, EmployeeSerializerAuth


class RegisterView(APIView, TemplateView):
    """
    Регистрация пользователей
    """
    template_name = "registration.html"
    permission_classes = []
    serializer_class = EmployeeSerializer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        positions = dict(POSITION_CHOICES)
        context["positions"] = positions
        return context

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                validate_password(request.data["password"])
            except Exception as password_errors:
                errors = []
                for error in password_errors:
                    errors.append(error)
                response = {
                    "Status": False,
                    "Errors": errors
                }
                return Response(data=response, status=HTTP_400_BAD_REQUEST)

            serializer.save()
            response = {
                "message": "User created successfully",
                "data": serializer.data
            }
            return Response(data=response, status=HTTP_201_CREATED)
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)


class AuthView(LoginView):
    """
    Аунтификацуя пользователей
    """
    template_name = "login.html"
    permission_classes = []
    serializer_class = EmployeeSerializerAuth
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse_lazy("main-menu")


def logout_user(request):
    """
    Выход из профиля
    """
    logout(request)
    return redirect("main-screen")
