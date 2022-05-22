from django.db import models

# Create your models here.


class Coins(models.Model):
    title = models.CharField('Название', max_length=10)
    author = models.CharField('Создатель', max_length=50)
    consensus = models.ForeignKey('Consensus', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Криптовалюта'
        verbose_name_plural = 'Криптовалюты'
        ordering = ['pk']


class Consensus(models.Model):
    title = models.CharField('Алгоритм консенсуса', max_length=50, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Алгоритм консенсуса'
        verbose_name_plural = 'Алгоритмы консенсуса'
        ordering = ['title']