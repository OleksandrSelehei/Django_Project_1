from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Product, Category
from cart.cart import Cart


class CategoryList:

    def get_category(self):
        return Category.objects.all()


class ProductsView(CategoryList, ListView):
    model = Product
    queryset = Product.objects.filter(draft=False)
    template_name = 'main/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        context['cart'] = cart
        return context


class DetailProductView(CategoryList, DetailView):
    model = Product
    slug_field = "url"

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        cart = Cart(request)
        cart.add_product_in_cart(product_id)
        return redirect('cart:basket')


class FilterProductsView(CategoryList, ListView):
    def get_queryset(self):
        queryset = Product.objects.filter(category__in=self.request.GET.getlist("category"))
        return queryset


def about_us(request):
    return render(request, 'main/about_us.html')


def contacts(request):
    return render(request, 'main/contacts.html')
