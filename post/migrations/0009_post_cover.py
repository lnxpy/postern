# Generated by Django 2.2.8 on 2020-01-27 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20200112_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, upload_to='post_image'),
        ),
    ]
