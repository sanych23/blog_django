from django.shortcuts import render
from .models import Products
from blog.models import User
from authorisation.widget import Widget
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from magazine.models import Cart
from django.http import HttpResponseRedirect, HttpResponse


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
            'user': user,
        })

    def cart(request):
        user = Widget.login_widget(request)
        cart = Widget.cart_widget(request)

        # user = User.objects.filter(email=request.session.get("user")).first()

        return render(request, "cart.html", context={
            'user': user,
            'cart': cart,
        })
    
    # @csrf_exempt
    # @api_view(["POST"])
    def update_cart(request, id):
        user = Widget.login_widget(request)

        if user:
            Cart.objects.create(product_id=id, user_id=user.id).save()
        else:
            response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            if request.COOKIES.get("products"):
                response.set_cookie('products', f'{request.COOKIES.get("products")}{id},', 3600)
            else:
                response.set_cookie('products', f'{id},', 3600)
            return response

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    def delete_from_cart(request, id):
        # print("delete")
        user = Widget.login_widget(request)

        if user:
            # Cart.objects.delete(product_id=id, user_id=user.id)
            Cart.objects.filter(product_id=id, user_id=user.id).delete()
        else:
            response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            response.set_cookie("products", request.COOKIES["products"].replace(f'{id},', ''))
            return response
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def product(request, id):
        user = Widget.login_widget(request)
        cart = Widget.cart_widget(request)

        product = Products.objects.get(id=id)

        # print(request.COOKIES.get("products"))
        return render(request, "product.html", context={
            "product": product,
            "cart": cart,
            "user": user,
        })