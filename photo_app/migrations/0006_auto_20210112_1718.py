# Generated by Django 3.1.5 on 2021-01-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_app', '0005_merge_20210111_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
