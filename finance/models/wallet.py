from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from finance.models.account import Currency


class PaymentMethod(models.Model):
    METHOD_TYPES = (
        ('debit', 'Debit Card'),
        ('credit', 'Credit Card'),
        ('cash', 'Cash')
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='payment_method'
    )

    bank_name = models.CharField(max_length=128, null=True, blank=True)
    account_number = models.CharField(max_length=128, unique=True, blank=True)
    card_number = models.CharField(unique=True, max_length=128, null=True, blank=True)
    card_type = models.CharField(max_length=10, choices=METHOD_TYPES, default=None)
    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    currency = models.ForeignKey(
        Currency,
        on_delete=models.DO_NOTHING,
        default=None
    )
    credit_limit = models.DecimalField(decimal_places=2, max_digits=10,
                                       validators=[MinValueValidator(0.00)],
                                       default=0.00)
    used_funds = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.card_type).capitalize()







