from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(max_length=300, verbose_name='Описание')
    image = models.ImageField(upload_to='media/', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = "Посты"

class Comment(models.Model):
    text = models.TextField(max_length=200, verbose_name="коментарий")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = "Коментарии"
