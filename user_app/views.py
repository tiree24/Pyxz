from django.shortcuts import render

from django.views import View

from photo_app.models import Image

class HomePage(View):
    html = 'homepage.html'
    def get(self, request):
        all_images = Image.objects.all()
        img_urls = [img.photo for img in all_images]
        return render(request, self.html, {'img_urls':img_urls})