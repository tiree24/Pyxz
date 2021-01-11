from django.shortcuts import render, redirect
from photo_app.models import Image, TaggableManager
from photo_app.forms import ImageForm


from comment_app.forms import CommentForm
from comment_app.models import Comment

from django.views import View

from taggit.models import Tag
from django.template.defaultfilters import slugify

from django.http import HttpResponseRedirect
# Create your views here.

from django.urls import reverse


def image_view(request, img_id):
    i = Image.objects.get(id=img_id)
    t = i.tags.all()
    return render(request, "image_detail.html", {"i": i, "t": t})


class AllTags(View):
    html = 'taglist.html'

    def get(self, request):
        tags = Image.tags.all()
        return render(request, self.html, {'taglist': tags})


class TagCategory(View):
    html = 'tagcategory.html'

    form = CommentForm()

    def get(self, request, tag_title):
        comments = Comment.objects.all()
        tag = Image.tags.get(slug=tag_title)
        images = Image.objects.filter(tags=tag)
        imgs = [img for img in images]
        return render(request, self.html, {'tag':tag,'imgList':imgs, 'form': self.form, 'comments': comments}) 

    def post(self, request, tag_title):
        form = CommentForm(request.POST)
        tag = Image.tags.get(name=tag_title)
        if form.is_valid():
            data = form.cleaned_data
            img = Image.objects.get(photo=request.POST.get("title", ""))
            model = Comment.objects.create(author=request.user, photo_linked=img, text=data['comment'])
            model.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



class ImageUpload(View):
    html = 'imageupload.html'

    def get(self, request):
        form = ImageForm()
        return render(request, 'imageupload.html', {'form': form})


    def post(self, request):
        form = ImageForm(request.POST, request.FILES)
        image = Image.objects.all()
        if form.is_valid():
            newimage = form.save(commit=False)
            newimage.myuser = request.user
            newimage.slug = slugify(newimage.title)
            newimage.save()
            form.save_m2m()
            return render(request, 'homepage.html', {'form': form})
        else:
            return render(request, self.html, {'form': form})


            # image = Image.objects.create(title= data['title'], 
            # photo = data['photo'], description = data['description'], 
            # tags = data['tags'], is_story = data['is_story'], myuser = request.user)
        
