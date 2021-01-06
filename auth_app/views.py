from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import View
# Create your views here.


class LoginFormView(View):

    form_class = LoginForm

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
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('Homepage'))
