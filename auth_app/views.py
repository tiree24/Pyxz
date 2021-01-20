from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect, render, reverse
from django.views.generic import View

from .forms import LoginForm


class LoginFormView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "login_view.html", { 'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('All')))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('All'))
