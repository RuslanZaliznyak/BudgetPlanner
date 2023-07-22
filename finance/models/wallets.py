from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    name = models.CharField(max_length=20)


class Wallet(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.ForeignKey(
        Currency,
        on_delete=models.DO_NOTHING,
        default=None
    )


class BankAccount(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.ForeignKey(
        Currency,
        on_delete=models.DO_NOTHING,
        default=None
    )
