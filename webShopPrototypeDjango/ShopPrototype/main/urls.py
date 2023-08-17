from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductsView.as_view()),
    path('catalog', views.ProductsView.as_view()),
    path('about_us', views.about_us),
    path('contacts', views.contacts),
    path('filter/', views.FilterProductsView.as_view(), name='filter'),
    path('add_to_cart/', views.DetailProductView.as_view(), name='add_to_cart'),
    path('<slug:slug>', views.DetailProductView.as_view(), name='product_detail')
]
