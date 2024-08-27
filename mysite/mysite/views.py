from django.shortcuts import render
import requests
from django.views import View


# Create your views here.
from blog.Data import *
from blog.models import *


class MySite(View):
    def action404(request):
        response = render(request, "error-404.html")
        response.status_code = 404
        return response