from django.urls import path
from django.views.generic import TemplateView

from .views import RegisterView, AuthView, ProjectView, logout_user, Task

urlpatterns = [
        path("", TemplateView.as_view(template_name='mainScreen.html'), name="main-screen"),
        path("main-menu/", TemplateView.as_view(template_name='mainMenu.html'), name="main-menu"),
        path("register/", RegisterView.as_view(), name="registration"),
        path("login/", AuthView.as_view(), name="login"),
        path("logout/", logout_user, name="logout"),
        path("create-project/", ProjectView.as_view(), name="create-project"),

        # view tasks
        path("tasks/", Task.view_tasks, name="user-tasks"),
        path("project/<str:project_id>/tasks/", Task.view_tasks, name="project-tasks"),

        # create task
        path("tasks/create/", Task.create_task, name="user-tasks-create"),
        path("project/<str:project_id>/tasks/create/", Task.create_task, name="project-tasks-create"),
]
