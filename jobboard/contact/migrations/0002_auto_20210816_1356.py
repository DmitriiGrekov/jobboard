# Generated by Django 3.2.6 on 2021-08-16 10:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='readed',
            field=models.BooleanField(default=False, verbose_name='Прочтено?'),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='sended_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
