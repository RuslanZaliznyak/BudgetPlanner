from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView

from finance.forms.transaction_form import TransactionForm
from finance.models.transaction import Transaction
from finance.services.data.account import AccountData
from finance.services.data.transaction import TransactionData
from finance.services.render.dashboard import Dashboard
from finance.services.render.transactions import TransactionsPage


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    @staticmethod
    def get_content(user_id):
        return {
            'transactions': TransactionData.get_all_by_user(user_id),
            'accounts': AccountData.get_all_by_user(user_id),
            'categories': TransactionData.get_all_categories(user_id),
            'expense_categories': [1, 2, 3]
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        context.update(self.get_content(user_id))
        return context


class TransactionsView(ListView):
    template_name = 'transactions/transactions.html'
    model = Transaction
    context_object_name = 'transactions'


class NewTransactionView(CreateView):
    template_name = 'transactions/new-transaction.html'
    form_class = TransactionForm
    success_url = '/finance/transactions'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        return super().form_valid(form)