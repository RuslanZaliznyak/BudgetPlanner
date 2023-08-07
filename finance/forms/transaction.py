from django import forms

from finance.models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction

        fields = (
            'category',
            'transaction_type',
            'amount',
            'description',
            'payment_method',
            'currency'
        )

        """widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'transaction_type': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control'}),
            'currency': forms.TextInput(attrs={'class': 'form-control'}),
        }"""

