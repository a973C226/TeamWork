from django.db import models

POSITION_CHOICES = (
    ('JR', 'Junior developer'),
    ('MD', 'Middle developer'),
    ('SR', 'Senior developer'),
    ('TL', 'Team Lead'),
)


# Регистрация и аутентификация пользователей.
# Управление профилем пользователя.
class Employee(models.Model):
    first_name = models.CharField(max_length=128, verbose_name='Имя')
    second_name = models.CharField(max_length=128, verbose_name='Фамилия')
    fam_name = models.CharField(max_length=128, null=True, blank=True, verbose_name='Отчество')
    login = models.EmailField(max_length=128, verbose_name='Логин')
    is_manager = models.BooleanField(default=False, verbose_name='Является ли пользователь менеджером')
    position = models.CharField(max_length=128, choices=POSITION_CHOICES, verbose_name='Должность')

    def __str__(self):
        username = f'{self.first_name} {self.second_name}'
        return username


# Создание, редактирование и удаление проектов.
# Назначение участников проекта и их ролей.
class Project(models.Model):
    pass

# Создание, редактирование и удаление задач.
# Отслеживание статуса задачи (открыта, в работе, завершена и т. д.).
# Присвоение задачи ответственному пользователю.
# Добавление комментариев к задаче.
# Прикрепление файлов к задаче.
class Task:
    pass

#Это сделать к диплому
class Board(models.Model):
    pass