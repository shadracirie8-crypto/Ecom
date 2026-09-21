from django.urls import path

from . import views


urlpatterns = [

    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    path(
        'success/',
        views.order_success,
        name='order_success'
    ),

    path(
        'my-orders/',
        views.my_orders,
        name='my_orders'
    ),
    
    path(
    'tracking/<int:order_id>/',
    views.order_tracking,
    name='order_tracking'
),

path(
    'receipt/<int:order_id>/',
    views.download_receipt,
    name='download_receipt'
),

]