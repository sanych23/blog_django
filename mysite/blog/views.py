from django.shortcuts import render, redirect
import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse, HttpResponseRedirect

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
                data["comments"] = post_comments
                
                post.view_count += 1
                post.save()
                # print('work')
                # if request.GET["status"]:
                match request.GET.get('status', False):
                    case "401":
                        data['status'] = "Post not found"
                    case "402":
                        data['status'] = "User not found"
                    case "403":
                        data['status'] = "Comment is empty"
        except:
            return redirect(MySite.action404)

        return render(request, "post.html", context=data)
    

    @csrf_exempt
    @api_view(["POST"])
    def newsletter(request):
        email = request.POST['email']

        if len(NewsLetter.objects.filter(email=email)) > 0:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            NewsLetter.objects.create(email=email)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

    @csrf_exempt
    @api_view(["POST"])
    def createComment(request):

        post = Posts.objects.filter(id=request.POST["post_id"]).exists()
        if not post:
            HttpResponseRedirect(f"{request.META.get('HTTP_REFERER')}?status=401#scroll_link")

        user = User.objects.filter(id=request.POST["author_id"]).exists()
        if not user:
            return HttpResponseRedirect(f"{request.META.get('HTTP_REFERER')}?status=402#scroll_link")

        if len(request.POST['content']) == 0:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        
        comment = Comment.objects.create(
            post_id=request.POST["post_id"],
            content=request.POST["content"],
            author_id=request.POST["author_id"],
        )
        comment.save()
        
        return redirect(f'/blog/post/{request.POST["post_id"]}?status=201#scroll_link')
