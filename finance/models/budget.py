from django.contrib.auth.models import User
from django.db import models


class LimitPeriod(models.Model):
    value = models.DurationField()


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default=None, blank=False, null=False)
    description = models.TextField(blank=True)
    daily_limit_amount = models.DecimalField(decimal_places=2, max_digits=10, default=None)
    limit_amount = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False)
    limit_period = models.ForeignKey(LimitPeriod, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f'{self.user} {self.daily_limit_amount} {self.limit_amount}')

