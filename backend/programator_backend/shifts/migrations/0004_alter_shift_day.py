# Generated by Django 4.2.6 on 2023-10-18 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0003_alter_day_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shifts.day'),
        ),
    ]
