from django.contrib.auth.models import User
from django.db import models

from finance.models.account import Currency
from finance.models.wallet import PaymentMethod


class Description(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value


class TransactionType(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense')
    )
    name = models.CharField(max_length=50, choices=TRANSACTION_TYPES)

    def __str__(self):
        return str(self.name).capitalize()


class TransactionCategory(models.Model):
    name = models.CharField(max_length=50)
    is_required = models.BooleanField(default=False)
    is_loan = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Transaction(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        TransactionCategory,
        on_delete=models.DO_NOTHING
    )
    transaction_type = models.ForeignKey(
        TransactionType,
        on_delete=models.DO_NOTHING
    )
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.ForeignKey(
        Description,
        on_delete=models.DO_NOTHING,
        null=True, blank=True
    )
    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.CASCADE
    )
    currency = models.ForeignKey(
        Currency,
        on_delete=models.DO_NOTHING,
        related_name='dashboard'
    )
    created_at = models.DateTimeField(auto_now_add=True)
