from decimal import Decimal
from django.conf import settings
from main.models import Product


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add_product_in_cart(self, product_id, quantity=1):
        if product_id in self.cart:
            self.cart[product_id] += quantity
        else:
            self.cart[product_id] = quantity
        self.save()

    def upgrade_product_in_cart(self, dictionary):
        self.cart = dictionary
        self.save()

    def delete_product_in_cart(self, product_id):
        del self.cart[product_id]
        self.save()

    def empty_trash(self):
        self.cart = {}
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
