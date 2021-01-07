from django.shortcuts import render, HttpResponseRedirect, reverse


from django.views import View

from photo_app.models import Image
from user_app.models import MyUser

from user_app.forms import SignUpForm

class HomePage(View):
    
    html = 'homepage.html'

    def get(self, request):
        img_set = Image.objects.all()
        return render(request, self.html, {'img_set': img_set})


class Profile(View):

    html = 'profile.html'

    def get(self, request, user_id):
        user = MyUser.objects.get(id=user_id)
        img_set = Image.objects.filter(myuser=user)
        return render(request, self.html, {'user':user,  'img_set':img_set })


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
            MyUser.objects.create_user(
                username=data['username'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=data['password']
            )
            return HttpResponseRedirect(reverse('Homepage'))

