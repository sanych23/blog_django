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
            print(products)

            return products
        else:
            return []

