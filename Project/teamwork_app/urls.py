from django.urls import path
from django.views.generic import TemplateView

from .views import RegisterView, AuthView, logout_user, Task, view_projects, SecureTemplateView, create_project, \
        view_tasks, create_task

urlpatterns = [
        path("", TemplateView.as_view(template_name='mainScreen.html'), name="main-screen"),
        path("main-menu/", SecureTemplateView.as_view(template_name='mainMenu.html'), name="main-menu"),
        path("register/", RegisterView.as_view(), name="registration"),
        path("login/", AuthView.as_view(), name="login"),
        path("logout/", logout_user, name="logout"),

        # посмотреть задачи
        path("tasks/", view_tasks, name="user-tasks"),
        path("project/<str:project_id>/tasks/", view_tasks, name="project-tasks"),

        # создать задачу
        path("main-menu/tasks/create/", create_task, name="user-tasks-create"),
        path("project/<str:project_id>/tasks/create/", create_task, name="project-tasks-create"),

        # посмотреть проект
        path("main-menu/projects/", view_projects, name="view-projects"),
        path("project/<str:project_id>/", view_projects, name="view-board"),

        # создать проект
        path("main-menu/create-project/", create_project, name="create-project"),
]
