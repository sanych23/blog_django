from django.contrib import admin
from django.urls import path

from blog.views import Blog


urlpatterns = [
    path("", Blog.home),
    path("postlist/", Blog.postList),
    path("post/<int:id>/", Blog.post),
]
