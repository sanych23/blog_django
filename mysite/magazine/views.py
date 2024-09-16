from django.shortcuts import render
from .models import Products

# Create your views here.
class InternetMagazine:
    def productList(request):
        products = Products.objects.all()

        return render(request, "productlist.html", context={
            "title": "Shop",
            "products": products,
        })

    def cart(request):
        return render(request, "cart.html")

    def product(request, id):
        product = Products.objects.get(id=id)

        # print(product.Images.all())

        return render(request, "product.html", context={
            "product": product,
        })