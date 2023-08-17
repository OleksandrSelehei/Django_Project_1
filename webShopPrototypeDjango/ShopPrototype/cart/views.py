from django.shortcuts import render, redirect
from main.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Orders, OrderItem
from .cart import Cart


def basket(request):
    data_cart = request.session['cart']
    product_ids = set(data_cart.keys())
    products = Product.objects.filter(id__in=product_ids)
    cart_items = []
    total_price = 0
    for key, value in data_cart.items():
        product = products.get(id=key)
        cart_item = {
            'product': product,
            'quantity': value,
        }

        price = product.price * value
        total_price += price

        cart_items.append(cart_item)

    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'cart/basket.html', context)


def delete(request):
    product_id = request.POST.get('product_id')
    cart = Cart(request)
    cart.delete_product_in_cart(product_id)
    return redirect('cart:basket')


@csrf_exempt
def update_data_cart(request):
    cart = Cart(request)
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        dictionary = json.loads(data)
        cart.upgrade_product_in_cart(dictionary)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


def order_page(request):
    return render(request, 'cart/order.html')


def buy(request):
    data_cart = request.session['cart']
    product_ids = set(data_cart.keys())
    products = Product.objects.filter(id__in=product_ids)
    print(data_cart)
    orders = Orders.objects.create(
        user_name=request.POST.get('user_name'),
        user_surname=request.POST.get('user_surname'),
        email=request.POST.get('email'),
        number_phone=request.POST.get('number_phone'),
        city=request.POST.get('city'),
        house_number=request.POST.get('house_number'),
        street=request.POST.get('street'),
    )
    for product in products:
        print(product.id)
        OrderItem.objects.create(order=orders, product=product, quantity=data_cart[str(product.id)])
    Cart(request).empty_trash()
    return redirect('cart:thanks_page')


def thanks_page(request):
    return render(request, 'cart/thanksgiving.html')

