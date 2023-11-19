from django.urls import path
from .views import RegisterView, AuthView

urlpatterns = [
        path("register/", RegisterView.as_view(), name="registration"),
        path("login/", AuthView.as_view(), name="login")
]
