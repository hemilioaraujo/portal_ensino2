# Generated by Django 3.1.5 on 2021-01-27 01:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20210126_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='data_nascimento',
            field=models.DateField(default=datetime.datetime.today, verbose_name='data nascimento'),
        ),
    ]