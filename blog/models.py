from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Тело поста')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    last_modified = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    categories = models.ManyToManyField('Category', related_name='posts', verbose_name='Категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)