# Generated by Django 3.1.5 on 2021-01-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_auto_20210112_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='bio',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]