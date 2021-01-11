"""pyxz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from user_app.views import HomePage, Profile, SignUp, NewView, TopView, FollowView, UnFollowView, FollowUserView
from photo_app.views import AllTags, Image_view, TagCategory, ImageUpload, LikeUpView, LikeDownView, StoryUpload
from auth_app.views import LoginFormView, LogoutView
from comment_app.views import CommentLikeUpView, CommentLikeDownView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='All'),
    path('new/', NewView.as_view(), name='New'),
    path('top/', TopView.as_view(), name='Top'),
    path('profile/<int:user_id>/', Profile.as_view(), name='Profile'),
    path('signup/', SignUp.as_view(), name='Signup'),
    path('listoftags/', AllTags.as_view(), name='Tags'),
    path('img/<int:img_id>', Image_view.as_view()),
    path('tag/<slug:tag_title>/', TagCategory.as_view(), name='TagSub'),
    path("login/", LoginFormView.as_view(), name="login"),
    path("logout/", LogoutView.as_view()),
    path("upload/", ImageUpload.as_view()),
    path("uploadstory/", StoryUpload.as_view()),
    path("likeup/<int:img_id>/", LikeUpView),
    path("likedown/<int:img_id>/", LikeDownView),
    path("follow/<int:user_id>/", FollowView),
    path("unfollow/<int:user_id>/", UnFollowView),
    path("commentlikeup/<int:comment_id>/", CommentLikeUpView), 
    path("commentlikedown/<int:comment_id>/", CommentLikeDownView),
    path("following/", FollowUserView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
