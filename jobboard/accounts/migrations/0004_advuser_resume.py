# Generated by Django 3.2.6 on 2021-08-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20210807_1824'),
        ('accounts', '0003_auto_20210809_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='advuser',
            name='resume',
            field=models.ManyToManyField(blank=True, null=True, to='jobs.ResumeModel', verbose_name='Отклики'),
        ),
    ]