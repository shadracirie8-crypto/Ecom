from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from shop.models import Product

from .models import Order, OrderItem

from .forms import OrderForm

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reportlab.pdfgen import canvas


# =========================
# CHECKOUT
# =========================
@login_required
def checkout(request):

    cart = request.session.get('cart', {})

    # PANIER VIDE
    if not cart:

        return redirect('cart_detail')

    cart_items = []

    total_price = 0

    # RECUPERATION PRODUITS
    for product_id, quantity in cart.items():

        product = Product.objects.get(
            id=product_id
        )

        subtotal = product.price * quantity

        total_price += subtotal

        cart_items.append({

            'product': product,

            'quantity': quantity,

            'subtotal': subtotal

        })

    # FORM
    form = OrderForm(

        initial={

            'full_name': request.user.username,

            'email': request.user.email

        }

    )

    # SUBMIT
    if request.method == 'POST':

        form = OrderForm(request.POST)

        if form.is_valid():

            # CREATE ORDER
            order = form.save(commit=False)

            order.user = request.user

            order.total_price = total_price

            order.save()

            # CREATE ORDER ITEMS
            for item in cart_items:

                OrderItem.objects.create(

                    order=order,

                    product=item['product'],

                    quantity=item['quantity'],

                    price=item['product'].price,

                    subtotal=item['subtotal']

                )

            # CLEAR CART
            request.session['cart'] = {}

            # SUCCESS MESSAGE
            messages.success(

                request,

                "Commande enregistrée avec succès !"

            )

            return redirect(

                'order_success'

            )

    context = {

        'form': form,

        'cart_items': cart_items,

        'total_price': total_price

    }

    return render(

        request,

        'orders/checkout.html',

        context

    )


# =========================
# SUCCESS PAGE
# =========================
@login_required
def order_success(request):

    return render(

        request,

        'orders/order_success.html'

    )


# =========================
# MY ORDERS
# =========================
@login_required
def my_orders(request):

    orders = Order.objects.filter(

        user=request.user

    )

    return render(

        request,

        'orders/my_orders.html',

        {

            'orders': orders

        }

    )
    
    
@login_required
def order_tracking(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(
        request,
        'orders/tracking.html',
        {
            'order': order
        }
    )
    



@login_required
def download_receipt(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = f'attachment; filename="receipt_{order.id}.pdf"'

    p = canvas.Canvas(response)

    # HEADER
    p.setFont("Helvetica-Bold", 20)
    p.drawString(100, 800, "ECO-SHOP RECEIPT")

    # INFOS
    p.setFont("Helvetica", 12)

    p.drawString(100, 760, f"Commande #: {order.id}")
    p.drawString(100, 740, f"Client: {order.full_name}")
    p.drawString(100, 720, f"Telephone: {order.phone}")
    p.drawString(100, 700, f"Ville: {order.city}")

    # PRODUCTS
    y = 650

    for item in order.items.all():

        p.drawString(
            100,
            y,
            f"{item.product.title} x{item.quantity} - {item.price} FCFA"
        )

        y -= 25

    # TOTAL
    p.setFont("Helvetica-Bold", 16)

    p.drawString(
        100,
        y - 30,
        f"TOTAL : {order.total_price} FCFA"
    )

    p.save()

    return response