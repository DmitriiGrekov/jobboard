# Generated by Django 3.2.6 on 2021-08-12 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_resumemessagemodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumemessagemodel',
            name='date_publish',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]