from django.shortcuts import render, redirect
from blog.models import Role
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from blog.models import User
import hashlib
from .services.token_generate import TokenGenerator
from django.http import HttpResponseRedirect
import os

# Create your views here.
class Auth:
    def login(request):
        return render(request, 'login.html')

    @csrf_exempt
    @api_view(["POST"])
    def loginform(request):
        password = hashlib.pbkdf2_hmac(
            'sha256',
            request.POST["password"].encode('utf-8'),
            bytes('секретик', 'utf-8'),
            100000
        )

        user = User.objects.filter(email=request.POST["email"], password=password).first()

        if not user:
            return redirect('/auth/login/')
        else:
            token = TokenGenerator.generate(user.email, user.username)
            user.token = token
            user.save()
            request.session["token"] = token
    
        return redirect('/magazine/cart/')

    def registration(request):
        roles = Role.objects.filter(hidden_role=False)

        return render(request, 'register.html', context={
            'roles': roles
        })
    
    @csrf_exempt 
    @api_view(["POST"]) 
    def registrationform(request): 
        user = User.objects.create(first_name = request.POST["first_name"], 
                                        last_name = request.POST["last_name"], 
                                        username = request.POST["login"], 
                                        email = request.POST["email"], 
                                        password = hashlib.pbkdf2_hmac(
                                            'sha256',
                                            request.POST["password"].encode('utf-8'),
                                            bytes('секретик', 'utf-8'),
                                            100000
                                        ),
                                        # request.POST["password"], 
                                        role_id = request.POST["role_id"],
                                        token = TokenGenerator.generate(request.POST["email"], request.POST["login"]),
                                    ) 
        user.save() 
 
        return redirect(Auth.login)
    