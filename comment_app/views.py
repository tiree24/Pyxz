from django.shortcuts import render, redirect
from comment_app.models import Comment
from user_app.models import MyUser
# Create your views here.


def CommentLikeUpView(request, comment_id):
    target = Comment.objects.get(id=comment_id)
    auth_user = MyUser.objects.get(id=request.user.id)
    target.likes.add(auth_user)
    target.save()
    return redirect(request.META.get('HTTP_REFERER'))

def CommentLikeDownView(request, comment_id):
    target = Comment.objects.get(id=comment_id)
    auth_user = MyUser.objects.get(id=request.user.id)
    target.likes.remove(auth_user)
    target.save()
    return redirect(request.META.get('HTTP_REFERER'))