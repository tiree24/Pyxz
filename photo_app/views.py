from django.shortcuts import render
from photo_app.models import Image, TaggableManager

from django.views import View
# Create your views here.


def image_view(request, img_id):
    i = Image.objects.get(id=img_id)
    return render(request, "image_detail.html", {"i": i})


class AllTags(View):
    html = 'taglist.html'

    def get(self, request):
        tags = Image.tags.all()
        return render(request, self.html, {'taglist':tags})
