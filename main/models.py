from django.db import models


# Create your models here.
#  python taskmanager\manage.py make migrations создать таблицы
# python taskmanager\manage.py migrate

# python taskmanager\manage.py createsuperuser

class Task(models.Model):  # бд
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title  # вывести имя поля

    class Meta:  # поменять имя
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
