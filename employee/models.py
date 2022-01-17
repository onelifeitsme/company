from department.models import Department
from django.contrib.auth.models import AbstractUser
from django.db import models
from position.models import Position
# Create your models here.
from django.urls import reverse
from pytils.translit import slugify
from multiselectfield import MultiSelectField
from autoslug import AutoSlugField
from datetime import date
from dateutil.relativedelta import relativedelta

# Create your models here.
class Employee(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    join_date = models.DateField('Дата устройства', auto_now_add=True)
    last_name = models.CharField('Фамилия', max_length=250)
    patronymic = models.CharField('Отчество', max_length=250)
    slug = models.SlugField(unique=True)
    photo = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)


    def experience(self):
        # ПОДСЧЁТ КОЛИЧЕСТВА ЛЕТ ПРЕБЫВАНИЯ В КОМПАНИИ
        delta = relativedelta(date.today() - self.join_date)
        return delta.years


    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('single_employee', args=[str(self.slug)])


    def save(self, *args, **kwargs):
        self.slug = slugify([self.username, self.last_name])
        super(Employee, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
#