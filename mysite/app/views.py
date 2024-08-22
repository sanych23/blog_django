from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from blog.models import Posts

from django.template import RequestContext

# Create your views here.
from django.http import HttpResponse
from django.views import View

import requests

from rest_framework.decorators import (
    api_view,
)


class Data:
    def getData(self):
        return [
            {"id": 1, "title": "заголовок 1", "content": "текст 1"},
            {"id": 2, "title": "заголовок 2", "content": "текст 2"},
            {"id": 3, "title": "заголовок 3", "content": "текст 3"},
        ]


class MainView(View):

    def action_igor(request):
        return HttpResponse("Hello, World!")

    @csrf_exempt
    @api_view(["POST"])
    def test_get(request):

        return HttpResponse("123213")

    def dataForm(request, *args, **kwargs):
        return HttpResponse(request.POST["login"])

    def handler404(request):
        response = render(request, "404.html")
        response.status_code = 404
        return response

    def news(request, id):
        data = {}

        for item in Data().getData():
            if item["id"] == id:
                data["news"] = item

        if len(data) == 0:
            return redirect("/error-404/")

        return render(request, "news.html", data)

    def start(request):

        x = 10
        y = 20

        data = {"x": x, "y": y}

        data["news"] = Data().getData()

        response = requests.get("https://liblessons.ru/ajax/data1.php")

        data["news_json"] = response.json()

        # return HttpResponse(response)
        return render(request, "start.html", data)
