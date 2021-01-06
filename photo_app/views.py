from django.shortcuts import render
from photo_app.models import Image, TaggableManager

from comment_app.forms import CommentForm
from comment_app.models import Comment

from django.views import View
# Create your views here.


def image_view(request, img_id):
    i = Image.objects.get(id=img_id)
    return render(request, "image_detail.html", {"i": i})


class AllTags(View):
    html = 'taglist.html'

    def get(self, request):
        user_id = request.user.id
        tags = Image.tags.all()
        return render(request, self.html, {'taglist':tags, 'user_id':user_id})


class TagCategory(View):
    html = 'tagcategory.html'

    form = CommentForm()
    comments = Comment.objects.all()

    def get(self, request, tag_title):
        user_id = request.user.id
        tag = Image.tags.get(name=tag_title)
        images = Image.objects.filter(tags=tag)
        imgs = [img for img in images]
        return render(request, self.html, {'tag':tag,'imgList':imgs, 'user_id':user_id, 'form': self.form, 'comments': self.comments}) 
