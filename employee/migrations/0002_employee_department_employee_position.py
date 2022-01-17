# Generated by Django 4.0.1 on 2022-01-17 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0001_initial'),
        ('department', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='position.position'),
            preserve_default=False,
        ),
    ]