from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from teamwork_app.forms import CreateProjectForm
from teamwork_app.models import Project


@login_required
def view_projects(request, project_id=None):
    """
    Просмотр проекта
    """
    user_id = request.user.id
    if project_id is not None:
        project = Project.objects.get(project=project_id)
        context = {"project": project}
        return render(request, "taskBoard.html", context)
    else:
        projects = Project.objects.filter(employee=user_id)
        context = {"projects": projects}
        return render(request, "viewProjectsList.html", context)


@login_required
def create_project(request):
    """
    Создание проекта
    """
    form = CreateProjectForm()

    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            # автовыбор текущего сотрудника
            form.instance.creator = request.user
            form.save()
            messages.success(request, "Проект успешно создан")
            return redirect("main-menu")

    context = {"form": form, "form_title": "Создание проекта", "submit_btn_text": "Создать проект"}

    return render(request, "baseForm.html", context)
