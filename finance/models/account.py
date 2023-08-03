from django.contrib.auth.models import User
from django.db import models

from finance.models.budget import Budget
from finance.models.loan import Loan
from finance_manager import settings


class Currency(models.Model):
    CURRENCY_LIST = (
        ('usd', 'American Dollar'),
        ('eur', 'Euro'),
        ('pln', 'Polish zloty')
    )
    code = models.CharField(max_length=3, choices=CURRENCY_LIST, unique=True)

    def __str__(self):
        return self.code


class Account(models.Model):
    ACCOUNT_TYPES = (
        ('personal', 'Personal account'),
        ('business', 'Business account')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=False, null=False)
    main_currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    description = models.CharField(max_length=128, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    account_type = models.CharField(max_length=20, null=False, blank=False,
                                    choices=ACCOUNT_TYPES)

    payment_methods = models.ManyToManyField('PaymentMethod',
                                             blank=True)
    loans = models.ManyToManyField(Loan, blank=True)
    budgets = models.ManyToManyField(Budget, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
