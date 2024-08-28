from django.shortcuts import render
import requests
from django.views import View
from django.conf import settings
from django.utils import translation
from django.http import HttpResponseRedirect



# Create your views here.
from blog.Data import *
from blog.models import *


class MySite(View):
    def action404(request):
        response = render(request, "error-404.html")
        response.status_code = 404
        return response
    
    def lang(request):
        code = request.GET.get('language')
        response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/blog/'))

        flag_check = False
        for lang in settings.LANGUAGES:
            if code in lang:
                flag_check = True
                break

        if code and translation.check_for_language(code) and flag_check:
            if hasattr(request, 'session'):
                request.session['django_language'] = code
                request.session['_language'] = code
            # else:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, code)
            translation.activate(code)
            print(f"Language is changed on {code}!")
        else:
            return HttpResponseRedirect('/custom-error-404/')
        return response

# sample
# def select_lang(request, code):
#     go_next = request.META.get('HTTP_REFERER', '/')
#     response = HttpResponseRedirect(go_next)
#     if code and translation.check_for_language(code):
#         if hasattr(request, 'session'):
#             request.session['django_language'] = code
#         else:
#             response.set_cookie(settings.LANGUAGE_COOKIE_NAME, code)
#         translation.activate(code)
#     return response
