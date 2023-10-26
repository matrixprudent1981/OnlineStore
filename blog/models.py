from django.db import models

from blog.constans import TYPE_BOOK


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


class Hashtag(models.Model):
    title = models.CharField(max_length=64)
    titl2 = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title} - {self.titl2}"

    class Meta:
        verbose_name = "Хештег"
        verbose_name_plural = 'Хештеги'


class PostTest(models.Model):
    ''' References'''

    hashtags = models.ManyToManyField(Hashtag)

    ''' Base field '''

    title = models.CharField(max_length=400, null=True)
    image = models.ImageField(upload_to='media/', null=True)
    description = models.TextField(null=True)
    tipe_book = models.CharField(max_length=100, choices=TYPE_BOOK, null=True)
    cost = models.PositiveIntegerField(null=True)
    director = models.CharField(max_length=100, null=True)
    number_of_page = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return (f'Название книги {self.title}\n'
                f'Цена книги {self.cost}')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'