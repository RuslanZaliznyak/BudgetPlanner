from django.contrib.auth.models import User
from django.db import models


class PaymentMethod(models.Model):
    method = models.CharField(max_length=15)

    def __str__(self):
        return self.method


class Description(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value


class TransactionType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TransactionCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    category_id = models.ForeignKey(
        TransactionCategory,
        on_delete=models.DO_NOTHING)

    transaction_type_id = models.ForeignKey(
        TransactionType,
        on_delete=models.DO_NOTHING)

    amount = models.DecimalField(decimal_places=2, max_digits=10)

    description_id = models.ForeignKey(
        Description,
        on_delete=models.DO_NOTHING
    )

    payment_method_id = models.ForeignKey(
        PaymentMethod,
        on_delete=models.DO_NOTHING
    )

    datetime = models.DateTimeField()

