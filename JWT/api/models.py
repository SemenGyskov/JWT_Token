from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    author = models.CharField(max_length=100, verbose_name='Автор')
    year = models.IntegerField(verbose_name='Год выпуска')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название списка')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая цена')
    class Meta:
        verbose_name = 'Заказанная книга'
        verbose_name_plural = 'Заказанные книги'
