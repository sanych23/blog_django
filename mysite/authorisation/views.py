from django.shortcuts import render, redirect
from blog.models import Role

# Create your views here.
class Auth:
    def login(request):
        return render(request, 'login.html')

    def loginform(request):
        return redirect(Auth.login)

    def registration(request):
        roles = Role.objects.filter(hidden_role=False)

        return render(request, 'register.html', context={
            'roles': roles
        })
    
    def registrationform(request):
        return redirect(Auth.login)
    