from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from teamwork_app.models import Employee, Task, Project

from teamwork_app.forms import CreateTaskForm


@login_required
def view_tasks(request, project_id=None):
    user_id = request.user.id
    if project_id is not None:
        tasks = Task.objects.filter(executor=user_id, project=project_id)
    else:
        tasks = Task.objects.filter(executor=user_id)
    context = { 'tasks': tasks }
    return render(request, 'taskTable.html', context)


@login_required
def create_task(request, project_id=None):
    form = CreateTaskForm()
    if project_id is not None:
        # автовыбор проекта и деактивация поля
        project = Project.objects.get(id=project_id)
        projects = [(project.id, project.name)]
        form.fields['project']._set_choices(projects)
        form.fields['project'].disabled = True
        # можно выбрать исполнителя из списка сотрудников, добавленных в проект
        employees = Employee.objects.filter(project=project_id)
        employees = [(employee.id, employee.__str__()) for employee in employees]
        form.fields['executor']._set_choices([('', '---------')] + employees)

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Задача успешно создана')
            return redirect('main-menu')

    context = {
        'form': form
    }

    return render(request,'createTaskCopy.html', context)
