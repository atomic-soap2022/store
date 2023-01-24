from django.urls import path
from apps.order.views import add_to_cart
from apps.order.views import cart_view,create_order_view


urlpatterns = [
    path('cart_view/',cart_view, name='cart_view'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('create/', create_order_view, name='create_order'),

]
