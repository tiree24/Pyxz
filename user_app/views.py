from django.shortcuts import render, HttpResponseRedirect, reverse

from django.views import View

from photo_app.models import Image
from user_app.models import MyUser

from user_app.forms import SignUpForm

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


class SignUp(View):

    form_class = SignUpForm

    def get(self, request):
        html = 'generic_form.html'
        form = self.form_class
        context = {'form': form}
        return render(request, html, context)

    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MyUser.objects.create(
                username=data['username'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=data['password'],
            )
            return HttpResponseRedirect(reverse('Home'))

