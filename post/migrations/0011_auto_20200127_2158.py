# Generated by Django 2.2.8 on 2020-01-27 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20200127_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, upload_to='post_image'),
        ),
    ]
