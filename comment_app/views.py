from django.shortcuts import redirect
from user_app.models import MyUser

from comment_app.models import Comment

from django.contrib.auth.decorators import login_required
# Create your views here.

# Create your views here.


@login_required
def CommentLikeUpView(request, comment_id):
    target = Comment.objects.get(id=comment_id)
    auth_user = MyUser.objects.get(id=request.user.id)
    target.likes.add(auth_user)
    target.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def CommentLikeDownView(request, comment_id):
    target = Comment.objects.get(id=comment_id)
    auth_user = MyUser.objects.get(id=request.user.id)
    target.likes.remove(auth_user)
    target.save()
    return redirect(request.META.get('HTTP_REFERER'))
