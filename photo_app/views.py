from django.shortcuts import render
from photo_app.models import Image


# Create your views here.


def image_view(request, img_id):
    i = Image.objects.get(id=img_id)
    return render(request, "image_detail.html", {"i": i})
