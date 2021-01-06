from django.shortcuts import render, redirect
from photo_app.models import Image, TaggableManager
from photo_app.forms import ImageForm
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

    def get(self, request, tag_title):
        user_id = request.user.id
        tag = Image.tags.get(name=tag_title)
        images = Image.objects.filter(tags=tag)
        img_urls = [url.photo for url in images]
        return render(request, self.html, {'tag':tag,'img_urls':img_urls, 'user_id':user_id}) 


class ImageUpload(View):
    html = 'imageupload.html'

    def get(self, request):
        form = ImageForm()
        return render(request, 'imageupload.html', {'form': form})


    def post(self, request):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Image.objects.create(title= data['title'], 
            photo = data['photo'], description = data['description'], 
            tags = data['tags'], is_story = data['is_story'], myuser = request.user)
            return render(request, 'homepage.html', {'form': form})
        else:
            return render(request, self.html, {'form': form})
