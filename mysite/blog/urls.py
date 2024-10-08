from django.contrib import admin
from django.urls import path

from blog.views import Blog


urlpatterns = [
    path("", Blog.home),
    path("postlist/", Blog.postList),
    path("create-comment/", Blog.createComment),
    path("post/<int:id>/", Blog.post),
    path("newsletter/", Blog.newsletter, name='newsletter'),
]
