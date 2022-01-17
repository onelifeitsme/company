from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.urls import reverse
from pytils.translit import slugify
from multiselectfield import MultiSelectField
from autoslug import AutoSlugField
from datetime import date
from dateutil.relativedelta import relativedelta


# Create your models here.
class Department(models.Model):
    name = models.CharField('Название', max_length=100, unique=True)
    slug = models.SlugField(auto_created=True)

    def get_absolute_url(self):
        return reverse('single_department', args=[str(self.slug)])


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
