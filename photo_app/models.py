from django.db import models
# Create your models here.
from user_app.models import MyUser
from taggit.managers import TaggableManager
from django.utils import timezone


class Image(models.Model):
    myuser = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=144)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='i')
    likes = models.ManyToManyField(MyUser, related_name='likes')
    post_time = models.DateTimeField(default=timezone.now)
    is_story = models.BooleanField()
    tags = TaggableManager()

    def __str__(self):
        return self.title

# Display for this many hours (int field)
# Story (boolean field)  ← notifications BooleanField
# comments = models.ForiegnKey(MyUser, on_delete=models.CASCADE)
# image = models.ForiegnKey(Image, on_delete=models.CASCADE)
