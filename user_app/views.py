import datetime

import pytz
from comment_app.forms import CommentForm
from comment_app.models import Comment
from django.db.models import Count, Q
from django.shortcuts import HttpResponseRedirect, render, reverse
from django.views import View
from django.views.generic import ListView
from photo_app.models import Image

from user_app.forms import SignUpForm, UserEditForm
from user_app.models import MyUser


class HomePage(View):

    html = 'homepage.html'
    form = CommentForm()

    def get(self, request):
        comments = Comment.objects.all()
        """ add this to views with all pictures except for stories """
        img_set = Image.objects.filter(is_story=False).all()
        # stories = Image.objects.filter(is_story=True).all()
        current_time = datetime.datetime.now(pytz.utc)

        def maths(current_time, post_time):
            numofdays = current_time - post_time
            return numofdays.days
        stories = [img for img in Image.objects.filter(is_story=True).all() if maths(current_time, img.post_time) <= 1]
        tags = Image.tags.all()
        context = {'img_set': img_set, 'comments': comments, 'form': self.form, 'stories': stories, 'taglist': tags}
        return render(request, self.html, context)

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            img = Image.objects.get(photo=request.POST.get("title", ""))
            model = Comment.objects.create(author=request.user, photo_linked=img, text=data['comment'])
            model.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class OrderedView(View):

    html = 'homepage.html'
    form = CommentForm()

    def get(self, request, order_by):
        comments = Comment.objects.all()
        img_set = Image.objects.filter(is_story=False).all().order_by(order_by)[::-1]
        current_time = datetime.datetime.now(pytz.utc)

        def maths(current_time, post_time):
            numofdays = current_time - post_time
            return numofdays.days
        stories = [img for img in Image.objects.filter(is_story=True).all() if maths(current_time, img.post_time) <= 1]
        tags = Image.tags.all()
        return render(request, self.html, {'img_set': img_set, 'comments': comments, 'form': self.form, 'stories': stories, 'taglist': tags})

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            img = Image.objects.get(photo=request.POST.get("title", ""))
            model = Comment.objects.create(author=request.user, photo_linked=img, text=data['comment'])
            model.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class TopView(View):

    html = 'homepage.html'
    form = CommentForm()

    def get(self, request):
        comments = Comment.objects.all()
        img_set = Image.objects.filter(is_story=False).all().annotate(like_count=Count('likes')).order_by('-like_count')
        current_time = datetime.datetime.now(pytz.utc)

        def maths(current_time, post_time):
            numofdays = current_time - post_time
            return numofdays.days
        stories = [img for img in Image.objects.filter(is_story=True).all() if maths(current_time, img.post_time) <= 1]
        return render(request, self.html, {'img_set': img_set, 'comments': comments, 'form': self.form, 'stories': stories})

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            img = Image.objects.get(photo=request.POST.get("title", ""))
            model = Comment.objects.create(author=request.user, photo_linked=img, text=data['comment'])
            model.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class FollowUserView(View):
    html = 'homepage.html'
    form = CommentForm()

    def get(self, request):
        following = request.user.following.all()
        comments = Comment.objects.all()
        img_set = Image.objects.filter(is_story=False).all().filter(myuser_id__in=following).all()
        current_time = datetime.datetime.now(pytz.utc)

        def maths(current_time, post_time):
            numofdays = current_time - post_time
            return numofdays.days
        stories = [img for img in Image.objects.filter(is_story=True).all() if maths(current_time, img.post_time) <= 1]
        tags = Image.tags.all()
        return render(request, self.html, {'img_set': img_set, 'comments': comments, 'form': self.form, 'stories': stories, 'taglist': tags})

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            img = Image.objects.get(photo=request.POST.get("title", ""))
            model = Comment.objects.create(author=request.user, photo_linked=img, text=data['comment'])
            model.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class FollowTagsView(View):
    html = 'homepage.html'
    form = CommentForm()

    def get(self, request):
        following = request.user.tags.all()
        comments = Comment.objects.all()
        img_set = Image.objects.filter(is_story=False).all().filter(tags__in=following).all()
        current_time = datetime.datetime.now(pytz.utc)

        def maths(current_time, post_time):
            numofdays = current_time - post_time
            return numofdays.days
        stories = [img for img in Image.objects.filter(is_story=True).all() if maths(current_time, img.post_time) <= 1]
        tags = Image.tags.all()
        return render(request, self.html, {'img_set': img_set, 'comments': comments, 'form': self.form, 'stories': stories, 'taglist': tags})

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            img = Image.objects.get(photo=request.POST.get("title", ""))
            model = Comment.objects.create(author=request.user, photo_linked=img, text=data['comment'])
            model.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


""" Follow this example to add photos/comments to any view """


class Profile(View):

    html = 'profile.html'
    form = CommentForm()

    def get(self, request, user_id):
        user = MyUser.objects.get(id=user_id)
        """ Need this if you want your filter photos by which user owns them """
        img_set = Image.objects.filter(is_story=False).all().filter(myuser=user)
        """ Need this or a way to capture your photos .all() or .get()"""
        comments = Comment.objects.all()
        return render(request, self.html, {'user': user,  'img_set': img_set, 'comments': comments, 'form': self.form})

    """ Copy the post() function fully """
    def post(self, request, user_id):
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            img = Image.objects.get(photo=request.POST.get("title", ""))
            model = Comment.objects.create(author=request.user, photo_linked=img, text=data['comment'])
            model.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


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
            return HttpResponseRedirect(reverse('All'))


class EditFormView(View):
    def get(self, request):
        form_data = {'bio': request.user.bio, 'tags': request.user.tags.all()}
        form = UserEditForm(initial=form_data, instance=request.user)
        html = 'generic_form.html'
        context = {'form': form}
        return render(request, html, context)

    def post(self, request):
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            data = form.cleaned_data
            custom_form = form.save(commit=False)
            custom_form.save()
            form.save_m2m()
            u = MyUser.objects.get(id=request.user.id)
            u.profile_pyxz = data['profile_pyxz']
            u.save()
            return render(request, 'homepage.html', {'form': form})


def funcView(request):
    if request.POST:
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            # data = form.cleaned_data
            custom_form = form.save(commit=False)
            custom_form.save()
            form.save_m2m()
            u = MyUser.objects.get(id=request.user.id)
            # u['profile_pyxz'] = request.POST['profile_pyxz'][0]
            u.save()
            breakpoint()
            return render(request, 'homepage.html', {'form': form})
    else:
        form_data = {'bio': request.user.bio, 'tags': request.user.tags.all()}
        form = UserEditForm(initial=form_data, instance=request.user)
        html = 'generic_form.html'
        context = {'form': form}
        return render(request, html, context)


def FollowView(request, user_id):
    user = MyUser.objects.get(id=user_id)
    request.user.following.add(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def UnFollowView(request, user_id):
    user = MyUser.objects.get(id=user_id)
    request.user.following.remove(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class SearchView(ListView):
    model = MyUser, Image
    template_name = 'search.html'

    def get(self, request):
        query = self.request.GET.get('q', None)
        if query is None:
            return render(self.request, 'search.html', {})

        object_list = MyUser.objects.filter(
            Q(username__icontains=query)
        )

        tag_list = Image.tags.filter(
            Q(slug__icontains=query))
        image_title = Image.objects.filter(
            Q(title__icontains=query))
        new_list = [x for x in object_list]
        new_list += [x for x in image_title]
        new_list += [x for x in tag_list]
        return render(self.request, 'search.html', {'new_list': new_list})


class UsersPageView(View):
    def get(self, request):
        html = 'users_page.html'
        displayuser = MyUser.objects.all()
        context = {'displayuser': displayuser}
        return render(request, html, context)
