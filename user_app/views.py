from django.shortcuts import render

from django.views import View

from photo_app.models import Image
from user_app.models import MyUser

class HomePage(View):
    html = 'homepage.html'
    def get(self, request):
        all_images = Image.objects.all()
        img_urls = [img.photo for img in all_images]
        user_id = request.user.id
        return render(request, self.html, {'img_urls':img_urls, 'user_id':user_id})


class Profile(View):
    html = 'profile.html'

    def get(self, request, user_id):
        user = MyUser.objects.get(id=user_id)
        user_pyxz = Image.objects.filter(myuser=user)
        pyxz_urls = [pyxz.photo for pyxz in user_pyxz]
        return render(request, self.html, {'user':user, 'num_of_followers':len(user.following.all()), 'img_urls':pyxz_urls, 'user_id':user_id})
