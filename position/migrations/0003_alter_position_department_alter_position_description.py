# Generated by Django 4.0.1 on 2022-01-18 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_alter_department_options'),
        ('position', '0002_position_vacant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department', verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='position',
            name='description',
            field=models.TextField(blank=True, max_length=500, verbose_name='Обязанности'),
        ),
    ]
