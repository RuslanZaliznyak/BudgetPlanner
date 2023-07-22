from django.contrib.auth.models import User
from django.db import models


class MandatoryPayments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    start_date = models.DateField()
    end_date = models.DateField()
    payment_day = models.PositiveIntegerField(default=None)
    is_active = models.BooleanField(default=True)
