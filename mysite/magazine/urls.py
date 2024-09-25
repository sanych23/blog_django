from django.contrib import admin
from django.urls import path

from .views import InternetMagazine


urlpatterns = [
    # path("", Blog.home),
    path("product-list/", InternetMagazine.productList),
    path("cart/", InternetMagazine.cart),
    path("product/<int:id>/", InternetMagazine.product),
    path("update-cart/<int:id>/", InternetMagazine.update_cart),
    path("delete-cart/<int:id>", InternetMagazine.delete_from_cart),
]
