# Generated by Django 3.1.5 on 2021-01-11 15:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment_app', '0002_auto_20210106_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comementlikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
