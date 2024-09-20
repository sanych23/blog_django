from django.shortcuts import render
from .models import Products
from blog.models import User


# Create your views here.
class InternetMagazine:
    def productList(request):
        products = Products.objects.all()

        return render(request, "productlist.html", context={
            "title": "Shop",
            "products": products,
        })

    def cart(request):
        user = User.objects.filter(email=request.session.get("user")).first()

        return render(request, "cart.html", context={
            'user': user,
        })

    def product(request, id):
        product = Products.objects.get(id=id)

        # print(product.Images.all())

        return render(request, "product.html", context={
            "product": product,
        })