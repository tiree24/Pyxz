from django.db import models

from user_app.models import MyUser
from photo_app.models import Image

from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='author')
    photo_linked = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='photo_linked')
    text = models.TextField(max_length=250)
    likes = models.ManyToManyField(MyUser, related_name='comementlikes')
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.author)