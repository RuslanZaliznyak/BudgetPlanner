from django import forms
from finance.models.account import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
