from django.contrib.auth.models import User
from django.db import models


class LimitPeriod(models.Model):
    value = models.DurationField()


class Budget(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    name = models.CharField(max_length=50, default=None)

    daily_limit_amount = models.DecimalField(decimal_places=2, max_digits=10,
                                             default=None)

    limit_amount = models.DecimalField(decimal_places=2, max_digits=10,)

    limit_period_id = models.ForeignKey(
        LimitPeriod,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return str(f'{self.user_id} {self.daily_limit_amount} {self.limit_amount}')

