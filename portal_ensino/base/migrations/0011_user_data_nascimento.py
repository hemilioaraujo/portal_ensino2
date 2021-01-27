# Generated by Django 3.1.5 on 2021-01-27 01:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_user_data_nascimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='data_nascimento',
            field=models.DateField(default=datetime.date.today, verbose_name='data nascimento'),
        ),
    ]
