# Generated by Django 2.2.8 on 2020-01-12 09:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_auto_20200112_0933'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='AdminProfile',
        ),
    ]
