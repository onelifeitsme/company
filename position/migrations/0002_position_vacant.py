# Generated by Django 4.0.1 on 2022-01-17 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='vacant',
            field=models.BooleanField(default=True, verbose_name='Свободная должность'),
        ),
    ]
