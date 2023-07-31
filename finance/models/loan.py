from django.contrib.auth.models import User
from django.db import models


class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_name = models.OneToOneField('TransactionCategory', on_delete=models.CASCADE)
    principal_amount = models.DecimalField(decimal_places=2, max_digits=10)
    start_date = models.DateField()
    end_date = models.DateField()
    interest_rate = models.DecimalField(decimal_places=2, max_digits=5)
    is_active = models.BooleanField(default=True)
    payment_amount = models.DecimalField(decimal_places=2, max_digits=10)
    payment_day = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.loan_name} - {self.user}"
