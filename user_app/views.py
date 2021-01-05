from django.shortcuts import render

from django.views import View

class HomePage(View):
    html = 'base.html'
    def get(self, request):

        return render(request, self.html, {})