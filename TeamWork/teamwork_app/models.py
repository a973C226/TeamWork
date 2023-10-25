from django.db import models
from django_softdelete.models import SoftDeleteModel

POSITION_CHOICES = (
    ('JR', 'Junior developer'),
    ('MD', 'Middle developer'),
    ('SR', 'Senior developer'),
    ('TL', 'Team Lead'),
)


# Управление профилем пользователя.
class Employee(SoftDeleteModel):
    """
    Модель сотрудника
    """
    first_name = models.CharField(max_length=128, verbose_name='Имя')
    second_name = models.CharField(max_length=128, verbose_name='Фамилия')
    fam_name = models.CharField(max_length=128, null=True, blank=True, verbose_name='Отчество')
    login = models.EmailField(max_length=128, unique=True, verbose_name='Логин')
    is_superuser = models.BooleanField(default=False, verbose_name='Является ли пользователь менеджером')
    position = models.CharField(max_length=128, choices=POSITION_CHOICES, verbose_name='Должность')

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = "Список сотрудников"
        ordering = ('first_name',)


class Project(models.Model):
    pass


# Прикрепление файлов к задаче.(диплом)
class Task:
    pass


#Это сделать к диплому
class Board(models.Model):
    pass
