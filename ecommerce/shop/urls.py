from django.urls import path
from . import views

urlpatterns = [
     
    path('', views.Acceuil, name='acceuil'),

    path('index', views.index, name='index'),
    path('product/<int:product_id>/',
         views.detail,
         name='detail'),

    path('cart/',
         views.cart_detail,
         name='cart_detail'),

    path('add-to-cart/<int:product_id>/',
         views.add_to_cart,
         name='add_to_cart'),

    path('remove-item/<int:product_id>/',
         views.remove_item,
         name='remove_item'),

    path('decrease-quantity/<int:product_id>/',
         views.decrease_quantity,
         name='decrease_quantity'),

    path('get-cart-count/',
         views.get_cart_count,
         name='get_cart_count'),

]