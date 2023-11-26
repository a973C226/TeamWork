from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from teamwork_app.forms import CreateProjectForm, CreateTaskForm
from teamwork_app.models import Project, Task


@login_required
def view_projects(request, project_id=None):
    """
    Просмотр проекта
    """
    user_id = request.user.id
    if project_id is not None:
        form = CreateTaskForm()
        project = Project.objects.get(id=project_id)
        tasks = Task.objects.filter(project=project_id)
        context = {
            "project": project,
            "form": form,
            "form_first_col": [
                form["name"],
                form["project"],
                form["description"],
            ],
            "form_second_col": [
                form["status"],
                form["category"],
                form["executor"],
                form["priority"],
                form["deadline"],
            ],
            "form_action": "user-tasks-create",
            "todo": tasks.filter(status="TO DO").order_by("deadline"),
            "stopped": tasks.filter(status="Stopped").order_by("deadline"),
            "in_progress": tasks.filter(status="In progress").order_by("deadline"),
            "review": tasks.filter(status="Review").order_by("deadline"),
            "in_testing": tasks.filter(status="In testing").order_by("deadline"),
            "complete": tasks.filter(status="Complete").order_by("deadline"),
        }
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
