from department.models import Department
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.urls import reverse
from pytils.translit import slugify
from multiselectfield import MultiSelectField
from autoslug import AutoSlugField
from datetime import date
from dateutil.relativedelta import relativedelta


class Position(models.Model):
    name = models.CharField('Название', max_length=120)
    description = models.TextField('Обязанности', max_length=500)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    slug = models.SlugField(auto_created=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('single_position', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Position, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'