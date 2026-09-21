from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),

    path('products/', views.products, name='dashboard_products'),

    path('orders/', views.orders, name='dashboard_orders'),

    path('users/', views.users_list, name='dashboard_users'),

    path('categories/', views.categories, name='dashboard_categories'),
    
    path(
    'products/add/',
    views.add_product,
    name='add_product'
    ),

    path(
    'products/edit/<int:product_id>/',
    views.edit_product,
    name='edit_product'
    ),

    path(
    'products/delete/<int:product_id>/',
    views.delete_product,
    name='delete_product'
    ),

    path(
    'categories/add-ajax/',
    views.add_category_ajax,
    name='add_category_ajax'
    ),
    
    path(
    'orders/',
    views.orders,
    name='dashboard_orders'
    ),

    path(
    'orders/<int:order_id>/',
    views.order_detail,
    name='dashboard_order_detail'
    ),

    path(
    'orders/<int:order_id>/<str:status>/',
    views.change_order_status,
    name='change_order_status'
    ),

]