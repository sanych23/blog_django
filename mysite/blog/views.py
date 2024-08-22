from django.shortcuts import render
import requests

# Create your views here.
from blog.Data import *
from blog.models import *


class Blog:

    def home(request):
        return render(request, "index.html")


    def postList(request):
        data = {
            "posts": Posts.objects.all(),
            "category": CategoryPost.objects.all(),
        }

        return render(request, "postlist.html", data)


    def post(request, id):

        post = Posts.objects.get(id=id)
        post_comments = post.comment_set.all()

        data = {
            'post': post,
            'comments': post_comments,
        }

        return render(request, "post.html", context=data)

