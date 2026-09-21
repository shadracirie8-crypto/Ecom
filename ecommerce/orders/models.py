from django.db import models

from django.contrib.auth.models import User

from shop.models import Product


# =========================
# ORDER MODEL
# =========================
class Order(models.Model):

    STATUS_CHOICES = (

        ('RECU', 'Reçu'),

        ('VALIDE', 'Validé'),

        ('EN_COURS', 'En cours de livraison'),

        ('LIVRE', 'Livré'),

        ('ANNULE', 'Annulé'),

    )

    PAYMENT_CHOICES = (

        ('LIVRAISON', 'Paiement à la livraison'),

        ('MOBILE_MONEY', 'Mobile Money'),

    )

    # USER
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    # CLIENT INFOS
    full_name = models.CharField(
        max_length=255
    )

    phone = models.CharField(
        max_length=20
    )

    email = models.EmailField()

    # ADDRESS
    city = models.CharField(
        max_length=150
    )

    commune = models.CharField(
        max_length=150
    )

    address = models.TextField()

    note = models.TextField(
        blank=True,
        null=True
    )

    # PAYMENT
    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_CHOICES,
        default='LIVRAISON'
    )

    # TOTAL
    total_price = models.FloatField(
        default=0
    )

    # STATUS
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='RECU'
    )

    # DATES
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ['-created_at']

    def __str__(self):

        return f"Commande #{self.id} - {self.full_name}"


# =========================
# ORDER ITEMS
# =========================
class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(
        default=1
    )

    price = models.FloatField()

    subtotal = models.FloatField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.product.title} x {self.quantity}"