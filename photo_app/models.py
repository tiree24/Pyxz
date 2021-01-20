from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.
from user_app.models import MyUser


class Image(models.Model):
    myuser = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=144)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='static/i')
    likes = models.ManyToManyField(MyUser, related_name='likes', blank=True)
    post_time = models.DateTimeField(default=timezone.now)
    is_story = models.BooleanField()
    slug = models.SlugField(unique=True, max_length=100, null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def score(self):
        return len(self.likes.all())

    def get_class_name(self):
        return self.__class__.__name__


# Display for this many hours (int field)
# Story (boolean field)  ← notifications BooleanField
# comments = models.ForiegnKey(MyUser, on_delete=models.CASCADE)
# image = models.ForiegnKey(Image, on_delete=models.CASCADE)
