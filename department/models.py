from django.db import models
from django.urls import reverse
from pytils.translit import slugify



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


