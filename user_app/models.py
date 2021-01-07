from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    following = models.ManyToManyField(
        'self', related_name='follow', blank=True)
    websiteURL = models.URLField(null=False, blank=True)
    # set releted field to tags to allow user to view the things that interest them
    def __str__(self):
        return self.username

    def get_following(self):
        return ",".join([str(p) for p in self.following.all()])

    def get_following_num(self):
        return self.following.count()

