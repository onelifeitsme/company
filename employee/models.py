from department.models import Department
from django.contrib.auth.models import AbstractUser
from django.db import models
from position.models import Position
from django.urls import reverse
from pytils.translit import slugify
from datetime import date
from dateutil.relativedelta import relativedelta


class Employee(AbstractUser):
    """Модель сотрудника"""
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Должность', null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Отдел', null=True, blank=True)
    join_date = models.DateField('Дата устройства', auto_now_add=True)
    last_name = models.CharField('Фамилия', max_length=250)
    patronymic = models.CharField('Отчество', max_length=250)
    slug = models.SlugField(unique=True)
    photo = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)

    def experience(self):
        """Подсчёт количества пребывания лет в компании"""
        delta = relativedelta(date.today() - self.join_date)
        return delta.years

    def __str__(self):
        if self.last_name:
            return self.last_name
        else:
            return self.username

    def get_absolute_url(self):
        return reverse('single_employee', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        """Автоматическое добавление слага при создании объекта модели"""
        self.slug = slugify([self.username, self.last_name])
        super(Employee, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
