from blog.models import *
from magazine.models import Cart
from magazine.models import Products


class Widget:

    @staticmethod
    def login_widget(request):
        user = User.objects.filter(email=request.session.get('user')).first()

        if not user:
            user = False

        return user

    @staticmethod
    def cart_widget(request):
        user = User.objects.filter(email=request.session.get('user')).first()

        if user:
            products = Products.objects.filter(id__in=Cart.objects.filter(user_id=user.id).values_list('product_id', flat=True))
            return products
        else:
            id_products = request.COOKIES.get('products')
            if id_products is None:
                return []
            id_products = id_products.split(',')[0:-1]
            # print(id_products)

            products = Products.objects.filter(id__in=id_products)
            return products

