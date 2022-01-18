# Generated by Django 4.0.1 on 2022-01-18 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0003_alter_position_department_alter_position_description'),
        ('department', '0002_alter_department_options'),
        ('employee', '0004_alter_employee_department_alter_employee_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='department.department', verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='position.position', verbose_name='Должность'),
        ),
    ]
