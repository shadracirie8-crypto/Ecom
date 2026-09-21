from django.shortcuts import render, redirect, get_object_or_404

from django.http import JsonResponse

from django.contrib import messages

from django.contrib.auth.models import User

from shop.models import Product, Category

from .forms import ProductForm

from orders.models import Order


# =========================
# DASHBOARD
# =========================
def dashboard(request):

    products_count = Product.objects.count()

    users_count = User.objects.count()

    categories_count = Category.objects.count()

    products = Product.objects.all()[:5]

    context = {

        'products_count': products_count,

        'users_count': users_count,

        'categories_count': categories_count,

        'products': products,

    }

    return render(
        request,
        'dashboard/index.html',
        context
    )


# =========================
# PRODUITS
# =========================
def products(request):

    query = request.GET.get('search', '')

    if query:

        products = Product.objects.filter(
            title__icontains=query
        )

    else:

        products = Product.objects.all()

    context = {

        'products': products,
        'query': query

    }

    return render(
        request,
        'dashboard/products.html',
        context
    )


# =========================
# AJOUT PRODUIT
# =========================
def add_product(request):

    form = ProductForm()

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Produit ajouté avec succès !"
            )

            return redirect(
                'dashboard_products'
            )

    context = {

        'form': form

    }

    return render(
        request,
        'dashboard/add_product.html',
        context
    )


# =========================
# MODIFIER PRODUIT
# =========================
def edit_product(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    form = ProductForm(
        instance=product
    )

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Produit modifié avec succès !"
            )

            return redirect(
                'dashboard_products'
            )

    context = {

        'form': form,
        'product': product

    }

    return render(
        request,
        'dashboard/edit_product.html',
        context
    )


# =========================
# SUPPRIMER PRODUIT
# =========================
def delete_product(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    product.delete()

    messages.success(
        request,
        "Produit supprimé avec succès !"
    )

    return redirect(
        'dashboard_products'
    )


# =========================
# UTILISATEURS
# =========================
def users_list(request):

    users = User.objects.all()

    context = {

        'users': users

    }

    return render(
        request,
        'dashboard/users.html',
        context
    )


# =========================
# CATEGORIES
# =========================
def categories(request):

    categories = Category.objects.all()

    context = {

        'categories': categories

    }

    return render(
        request,
        'dashboard/categories.html',
        context
    )


# =========================
# COMMANDES
# =========================
def orders(request):

    return render(
        request,
        'dashboard/orders.html'
    )


# =========================
# AJOUT CATEGORY AJAX
# =========================
def add_category_ajax(request):

    if request.method == 'POST':

        name = request.POST.get('name')

        if name:

            # CHECK EXIST
            existing = Category.objects.filter(
                name__iexact=name
            ).first()

            if existing:

                return JsonResponse({

                    'success': True,

                    'id': existing.id,

                    'name': existing.name

                })

            # CREATE
            category = Category.objects.create(
                name=name
            )

            return JsonResponse({

                'success': True,

                'id': category.id,

                'name': category.name

            })

    return JsonResponse({

        'success': False

    })
    
    



# =========================
# COMMANDES
# =========================
def orders(request):

    status = request.GET.get('status')

    search = request.GET.get('search')

    orders = Order.objects.all().order_by('-created_at')

    # FILTER STATUS
    if status:

        orders = orders.filter(
            status=status
        )

    # SEARCH
    if search:

        orders = orders.filter(
            full_name__icontains=search
        )

    return render(

        request,

        'dashboard/orders.html',

        {

            'orders': orders

        }

    )


# =========================
# DETAIL COMMANDE
# =========================
def order_detail(request, order_id):

    order = Order.objects.get(
        id=order_id
    )

    return render(

        request,

        'dashboard/order_detail.html',

        {

            'order': order

        }

    )


# =========================
# CHANGE STATUS
# =========================
def change_order_status(request, order_id, status):

    order = Order.objects.get(
        id=order_id
    )

    order.status = status

    order.save()

    return redirect(
        'dashboard_orders'
    )