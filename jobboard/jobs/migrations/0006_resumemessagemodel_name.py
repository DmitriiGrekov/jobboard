# Generated by Django 3.2.6 on 2021-08-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_resumemessagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumemessagemodel',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Имя'),
        ),
    ]
