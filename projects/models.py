from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание')
    technology = models.CharField(max_length=20, verbose_name='Стек технологий')
    image = models.FilePathField(path='/img', verbose_name='Превью проекта')

    class Meta:
        verbose_name_plural = 'Проекты'
        verbose_name = 'Проект'