from django.db import models


# Create your models here.
class TvShow(models.Model):
    TYPE_TVSHOW = (
        ('Драма', 'Драма'),
        ('Мелодрама', 'Мелодрама'),
        ('Боевик', 'Боевик'),
        ('Вестерн', 'Вестерн'),
        ('Фэнтези', 'Фэнтези'),
        ('Исторические', 'Исторические'),
        ('Комедия', 'Комедия'),
    )
    title = models.CharField(max_length=100, verbose_name="Укажите названия фильма")
    description = models.TextField(verbose_name="Описание фильма", blank=True)
    image = models.ImageField(upload_to='films/', verbose_name="Фото фильма", blank=True)
    price = models.PositiveIntegerField(verbose_name="Укажите цену фильма", blank=True)
    genre = models.CharField(max_length=100, choices=TYPE_TVSHOW)
    author = models.CharField(max_length=100, verbose_name="Автор фильма", blank=True)
    trailer = models.URLField(verbose_name="Ссылка на трейлер")

    def __str__(self):
        return self.title
