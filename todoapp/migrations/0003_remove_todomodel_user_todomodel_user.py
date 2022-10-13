# Generated by Django 4.1.2 on 2022-10-13 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todoapp', '0002_todomodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todomodel',
            name='user',
        ),
        migrations.AddField(
            model_name='todomodel',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
