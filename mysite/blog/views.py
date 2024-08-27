from django.shortcuts import render, redirect
import requests

# Create your views here.
from blog.Data import *
from blog.models import *
from mysite.views import MySite


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
        data = {}

        try:
            post = Posts.objects.get(id=id)

            if post:
                post_comments = post.comment_set.all()
                data["post"] = post
                data["comments"] = post_comments,
                
                post.view_count += 1
                post.save()
            else:
                redirect("error-404/")
        except:
            return redirect(MySite.action404)

        return render(request, "post.html", context=data)

