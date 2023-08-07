from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView

from finance.forms.transaction_form import TransactionForm
from finance.models.transaction import Transaction
from finance.services.data.account import AccountData
from finance.services.data.transaction import TransactionData


class DashboardView(View):
    @staticmethod
    def get_content(user_id):
        return {
            'transactions': TransactionData.get_all_by_user(user_id),
            'accounts': AccountData.get_all_by_user(user_id),
            'categories': TransactionData.get_all_categories(user_id),
            'expense_categories': [1, 2, 3]
        }

    template = 'dashboard/dashboard.html'

    def get(self, request):
        return render(request,
                      template_name=self.template,
                      context=self.get_content(request.user.id))

    def post(self, request):
        if 'new-transactions' in request.post:
            print('new-t')


class TransactionsView(ListView):
    template_name = 'transactions/transactions.html'
    model = Transaction
    context_object_name = 'transactions'

    @classmethod
    def create_form(cls, request):
        pass


class NewTransactionView(CreateView):
    template_name = 'transactions/form.html'
    form_class = TransactionForm
    success_url = '/finance/transactions'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        return super().form_valid(form)
