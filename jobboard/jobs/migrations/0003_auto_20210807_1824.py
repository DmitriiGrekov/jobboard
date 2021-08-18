# Generated by Django 3.2.6 on 2021-08-07 15:24

from django.db import migrations, models
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20210807_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumemodel',
            name='portfolio_file',
            field=models.FileField(blank=True, null=True, upload_to=jobs.models.user_directory_path, verbose_name='Портфолио'),
        ),
        migrations.AlterField(
            model_name='resumemodel',
            name='portfolio_link',
            field=models.CharField(max_length=1000, verbose_name='Ссылка на портфолио'),
        ),
    ]
