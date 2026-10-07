from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Category, Product


# =========================================
# PAGE ACCUEIL
# =========================================



def Acceuil(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'shop/Acceuil.html', context)


def index(request):

    query = request.GET.get('search', '')

    if query:

        products = Product.objects.filter(
            title__icontains=query
        )

    else:

        products = Product.objects.all()

    # HTMX REQUEST
    if request.headers.get('HX-Request'):

        return render(
            request,
            'shop/product_list.html',
            {
                'products': products
            }
        )

    return render(
        request,
        'shop/index.html',
        {
            'products': products
        }
    )


# =========================================
# DETAIL PRODUIT
# =========================================
# =========================================
# DETAIL PRODUIT
# =========================================
def detail(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart = request.session.get('cart', {})

    current_quantity = cart.get(
        str(product_id),
        0
    )

    return render(
        request,
        'shop/details.html',
        {
            'product': product,
            'current_quantity': current_quantity,
        }
    )


# =========================================
# AJOUTER AU PANIER
# =========================================
def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    # SESSION
    cart = request.session.get('cart', {})

    product_id_str = str(product_id)

    # QUANTITE ACTUELLE
    current_qty = cart.get(product_id_str, 0)

    # STOCK CHECK
    if current_qty < product.stock:

        cart[product_id_str] = current_qty + 1

    # SAVE SESSION
    request.session['cart'] = cart

    # HTMX RESPONSE
    response = HttpResponse()

    # EVENT
    response["HX-Trigger"] = "cartUpdated"

    return response


# =========================================
# DIMINUER QUANTITE
# =========================================
def decrease_quantity(request, product_id):

    cart = request.session.get('cart', {})

    product_id_str = str(product_id)

    if product_id_str in cart:

        # DIMINUER
        if cart[product_id_str] > 1:

            cart[product_id_str] -= 1

        # SUPPRIMER
        else:

            del cart[product_id_str]

    # SAVE
    request.session['cart'] = cart

    # RESPONSE
    response = HttpResponse()

    response["HX-Trigger"] = "cartUpdated"

    return response


# =========================================
# SUPPRIMER ARTICLE
# =========================================
def remove_item(request, product_id):

    cart = request.session.get('cart', {})

    product_id_str = str(product_id)

    if product_id_str in cart:

        del cart[product_id_str]

    # SAVE
    request.session['cart'] = cart

    # RESPONSE
    response = HttpResponse()

    response["HX-Trigger"] = "cartUpdated"

    return response


# =========================================
# PAGE PANIER
# =========================================
def cart_detail(request):

    cart = request.session.get('cart', {})

    cart_items = []

    total_price = 0

    total_quantity = 0

    for product_id, quantity in cart.items():

        product = get_object_or_404(
            Product,
            id=product_id
        )

        subtotal = product.price * quantity

        total_price += subtotal

        total_quantity += quantity

        cart_items.append({

            'product': product,

            'quantity': quantity,

            'subtotal': subtotal

        })

    template = 'shop/cart.html'

    if request.headers.get('HX-Request'):

        template = 'shop/partials/cart_content.html'

    return render(
        request,
        template,
        {

            'cart_items': cart_items,

            'total_price': total_price,

            'total_quantity': total_quantity

        }
    )

# =========================================
# COMPTEUR PANIER
# =========================================
def get_cart_count(request):

    cart = request.session.get('cart', {})

    total_items = sum(cart.values())

    return HttpResponse(total_items)

def apropos(request):
    return render(request, 'shop/apropos.html')

def contact(request):
    return render(request, 'shop/contact.html')