from django import forms

"""
class Comment(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='author')
    photo_linked = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='photo_linked')
    text = models.TextField(max_length=250)
    likes = models.ManyToManyField(MyUser, related_name='comementlikes', blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.author)
"""


class CommentForm(forms.Form):
    comment = forms.CharField()
