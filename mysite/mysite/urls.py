"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from .views import MySite
from django.conf.urls.i18n import i18n_patterns
from app.views import MainView
from django.urls import include

urlpatterns = [
    path("", MainView.start),
    path("data-form/", MainView.dataForm),
    path("news/<int:id>/", MainView.news),
    path("admin/", admin.site.urls),
    path("igor/", MainView.action_igor),
    # path("error-404/", MainView.handler404),
    path("test-get/", MainView.test_get),
    path("blog/", include("blog.urls")),
    path("custom-error-404/", MySite.action404),
    path("lang/", MySite.lang),
    path("i18n/", include("django.conf.urls.i18n")),
]
