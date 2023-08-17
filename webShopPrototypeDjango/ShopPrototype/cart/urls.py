from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('basket', views.basket, name='basket'),
    path('order', views.order_page, name='order'),
    path('thanks_page', views.thanks_page, name='thanks_page'),
    path('buy', views.buy, name='buy'),
    path('delete', views.delete, name='delete'),
    path('update_cart', views.update_data_cart, name='update_cart')
]
