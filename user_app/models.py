from django.contrib.auth.models import AbstractUser
from django.db import models
from taggit.managers import TaggableManager



class MyUser(AbstractUser):
    following = models.ManyToManyField(
        'self', related_name='follow', blank=True)
    websiteURL = models.URLField(null=False, blank=True)
    profile_pyxz = models.ImageField(upload_to='static/i', null=True, blank=True)
    bio = models.CharField(max_length=500, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=100, null=True, blank=True)
    tags = TaggableManager()
    # set releted field to tags to allow user to view the things that interest them

    def __str__(self):
        return self.username

    def get_following(self):
        return ",".join([str(p) for p in self.following.all()])

    def get_following_num(self):
        return self.following.count()

    def get_class_name(self):
        return self.__class__.__name__

    def get_profilepic_status(self):
        return bool(self.profile_pyxz)
