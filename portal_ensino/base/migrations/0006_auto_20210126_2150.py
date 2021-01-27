# Generated by Django 3.1.5 on 2021-01-27 00:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_user_instituicao'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='data_nascimento',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='data nascimento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='instituicao',
            field=models.CharField(blank=True, max_length=150, verbose_name='instituição'),
        ),
    ]