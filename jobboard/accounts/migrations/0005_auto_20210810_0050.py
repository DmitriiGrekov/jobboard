# Generated by Django 3.2.6 on 2021-08-09 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20210807_1824'),
        ('accounts', '0004_advuser_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='advuser',
            name='jobs',
            field=models.ManyToManyField(blank=True, null=True, related_name='job', to='jobs.JobModel', verbose_name='Вакансии пользователя'),
        ),
        migrations.AlterField(
            model_name='advuser',
            name='favourits',
            field=models.ManyToManyField(blank=True, null=True, related_name='favourits', to='jobs.JobModel', verbose_name='Избранные вакансии'),
        ),
    ]
