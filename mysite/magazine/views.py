from django.shortcuts import render
from .models import Products
from blog.models import User
from authorisation.widget import Widget


# Create your views here.
class InternetMagazine:
    def productList(request):
        user = Widget.login_widget(request)
        cart = Widget.cart_widget(request)

        products = Products.objects.all()

        return render(request, "productlist.html", context={
            "title": "Shop",
            "products": products,
            'cart': cart,
        })

    def cart(request):
        user = Widget.login_widget(request)
        cart = Widget.cart_widget(request)

        # user = User.objects.filter(email=request.session.get("user")).first()

        return render(request, "cart.html", context={
            'user': user,
            'cart': cart,
        })

    def product(request, id):
        user = Widget.login_widget(request)
        cart = Widget.cart_widget(request)

        product = Products.objects.get(id=id)

        # print(product.Images.all())

        return render(request, "product.html", context={
            "product": product,
        })