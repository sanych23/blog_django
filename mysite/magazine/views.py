from django.shortcuts import render
from .models import Products
from blog.models import User
from authorisation.widget import Widget
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from magazine.models import Cart
from django.http import HttpResponseRedirect, HttpResponse
import json
import pprint


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
            # cart_obj = Cart.objects.update_or_create(product_id=id, user_id=user.id)
            # if cart_obj:
            #     print('exist')
            # else:
            #     print("not exists")

            # Cart.objects.update_or_create(product_id=id, user_id=user.id, defaults={
            #     "count": Cart.objects.get(product_id=id, user_id=user.id).count + 1
            # }, create_defaults={
            #     "product_id": id,
            #     "user_id": user.id,
            # })

            try:
                cart_obj = Cart.objects.get(product_id=id, user_id=user.id)
                cart_obj.count += 1
                cart_obj.save()
            except:
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
    
    @csrf_exempt
    @api_view(["POST"])
    def deleteProduct(request):
        print(request.body)
        s = json.loads(request.body)
        
        try:
            Cart.objects.get(product_id=s["id"], user_id=11).delete()
            return HttpResponse(json.dumps({"status": True}), content_type="application/json")
        except:
            return HttpResponse(json.dumps({"status": False}), content_type="application/json")
        
    @csrf_exempt
    @api_view(["POST"])
    def productsCart(request):
        cart = Widget.cart_widget(request)

        products= []
        for product in cart:
            products.append({
                "id": product.id,
                "title": product.title,
                "main_image_path": product.main_image_path(),
                "price": str(product.price),
                "count": Cart.objects.get(product_id=product.id, user_id=Widget.login_widget(request).id).count,
            })

        return HttpResponse(json.dumps(products), content_type="application/json")

    @csrf_exempt
    @api_view(["POST"]) 
    def change_cart(request):
        data = json.loads(request.body)
        for product in data:
            Cart.objects.filter(product_id=product["id"], user_id=Widget.login_widget(request).id).update(count=product["count"])
        return HttpResponse(json.dumps({"status": True}), content_type="application/json")

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