from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from teamwork_app.models import Employee, Task, Project

from teamwork_app.forms import CreateTaskForm


@login_required
def view_tasks(request, project_id=None):
    """
    Просмотр задач
    """
    user_id = request.user.id
    if project_id is not None:
        tasks = Task.objects.filter(project=project_id)
    else:
        tasks = Task.objects.filter(executor=user_id)
    form = CreateTaskForm()
    context = {
        "form": form,
        "form_first_col": [
            form["name"],
            form["description"],
        ],
        "form_second_col": [
            form["status"],
            form["executor"],
            form["priority"],
            form["deadline"],
        ],
        "todo": tasks.filter(status="TO DO").order_by("deadline"),
        "stopped": tasks.filter(status="Stopped").order_by("deadline"),
        "in_progress": tasks.filter(status="In progress").order_by("deadline"),
        "review": tasks.filter(status="Review").order_by("deadline"),
        "in_testing": tasks.filter(status="In testing").order_by("deadline"),
        "complete": tasks.filter(status="Complete").order_by("deadline"),
    }
    return render(request, "taskBoard.html", context)


@login_required
def create_task(request, project_id=None):
    """
    Создание задачи
    """
    if project_id is not None:
        form = CreateTaskForm()
        del form.fields["project"]
        employees = Employee.objects.filter(project=project_id)
    else:
        form = CreateTaskForm()
        employees = Employee.objects.all()

    # можно выбрать исполнителя из списка сотрудников, добавленных в проект
    employees = [(employee.id, employee.__str__()) for employee in employees]
    form.fields["executor"]._set_choices([("", "---------")] + employees)

    if request.method == "POST":
        if project_id is not None:
            form = CreateTaskForm(request.POST)
            del form.fields["project"]
        else:
            form = CreateTaskForm(request.POST)
        if form.is_valid():
            if project_id is not None:
                # автовыбор текущего проекта
                project = Project.objects.get(id=project_id)
                form.instance.project = project
            form.save()
            messages.success(request, "Задача успешно создана")
            return redirect("main-menu")

    context = {"form": form}

    return render(request, "createProject.html", context)
