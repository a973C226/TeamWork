from django.urls import path
from django.views.generic import TemplateView

from .views import RegisterView, AuthView

urlpatterns = [
        path("register/", RegisterView.as_view(), name="registration"),
        path("login/", AuthView.as_view(), name="login"),
        path("", TemplateView.as_view(template_name='mainScreen.html'), name="main-screen"),
]
