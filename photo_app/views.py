from django.shortcuts import render, redirect
from photo_app.models import Image, TaggableManager
from photo_app.forms import ImageForm
from user_app.models import MyUser

from comment_app.forms import CommentForm
from comment_app.models import Comment

from django.views import View

from taggit.models import Tag
from django.template.defaultfilters import slugify

from django.http import HttpResponseRedirect
# Create your views here.

from django.urls import reverse


class Image_view(View):
    
    def get(self, request, img_id):
        form = CommentForm()
        i = Image.objects.get(id=img_id)
        t = i.tags.all()
        comments = Comment.objects.filter(photo_linked_id=img_id)
        return render(request, "image_detail.html", {"i": i, "t": t, 'comments':comments, 'form': form})

    def post(self, request, img_id):
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            img = Image.objects.get(id=img_id)
            model = Comment.objects.create(author=request.user, photo_linked=img, text=data['comment'])
            model.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


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
        img_set = Image.objects.filter(tags=tag)
        """ Need this or a way to capture your photos .all() or .get()"""
        comments = Comment.objects.all()
        """ Need this """
        return render(request, self.html, {'tag':tag,'img_set': img_set, 'comments': comments, 'form': self.form}) 

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


def LikeUpView(request, img_id):
    target = Image.objects.get(id=img_id)
    auth_user = MyUser.objects.get(id=request.user.id)
    target.likes.add(auth_user)
    print(target.likes.all)
    target.save()
    return redirect(request.META.get('HTTP_REFERER'))

def LikeDownView(request, img_id):
    target = Image.objects.get(id=img_id)
    auth_user = MyUser.objects.get(id=request.user.id)
    target.likes.remove(auth_user)
    target.save()
    return redirect(request.META.get('HTTP_REFERER'))
