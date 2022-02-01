from department.models import Department
from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class Position(models.Model):
    """Модель должности"""
    name = models.CharField('Название', max_length=120)
    description = models.TextField('Обязанности', max_length=500, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Отдел')
    vacant = models.BooleanField('Свободная должность', default=True)
    slug = models.SlugField(auto_created=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('single_position', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        """Автоматическое добавление слага при создании объекта модели"""
        self.slug = slugify(self.name)
        super(Position, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
