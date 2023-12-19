from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from teamwork_app.models import Employee, Task, Project

from teamwork_app.forms import CreateTaskForm


@login_required
def view_tasks(request):
    """
    Просмотр задач
    """
    user_id = request.user.id
    form = CreateTaskForm()
    form_action = "project-tasks-create"
    tasks = Task.objects.filter(executor=user_id)
    projects = Project.objects.filter(employee=request.user.id)
    # Создать задачу можно только на тот проект, куда добавлен юзер
    projects = [(project.id, project.__str__()) for project in projects]
    form.fields["project"]._set_choices([("", "---------")] + projects)
    if request.user.is_manager:
        employees = Employee.objects.all()
    else:
        employees = Employee.objects.filter(id=user_id)
    employees = [(employee.id, employee.__str__()) for employee in employees]
    form.fields["executor"]._set_choices([("", "---------")] + employees)

    context = {
        "form": form,
        "form_first_col": [
            form["name"],
            form["status"],
            form["description"],
        ],
        "form_second_col": [
            form["category"],
            form["executor"],
            form["priority"],
            form["deadline"],
        ],
        "form_action": form_action,
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
        projects = Project.objects.filter(employee=request.user.id)
        # Создать задачу можно только на тот проект, куда добавлен юзер
        projects = [(project.id, project.__str__()) for project in projects]
        form.fields["project"]._set_choices([("", "---------")] + projects)

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

    context = {"form": form, "form_title": "Создание задачи", "submit_btn_text": "Создать задачу"}

    return render(request, "baseForm.html", context)


@login_required
def get_task(request, task_id):
    """
    Получение данных задачи для модального окна
    """
    task = Task.objects.get(id=task_id)

    executor_data = serializers.serialize("json", [task.executor])
    executor = {
        "name": task.executor.__str__(),
        "data": executor_data
    }
    task_data = {
        "name": task.name,
        "description": task.description,
        "status": task.status,
        "category": task.category,
        "executor": executor,
        "priority": task.priority,
        "deadline": task.deadline
    }

    return JsonResponse(task_data)


@login_required
def change_task(request, task_id):
    pass


@login_required
def delete_task(request, task_id):
    pass
