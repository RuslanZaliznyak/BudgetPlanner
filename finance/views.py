from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView

from finance.forms.transaction import TransactionForm
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


# Func who renders page with transactions forms - TO REDESIGN
def add_transactions(request):
    user_id = request.user.id
    context = {'form': TransactionForm(),
               'transactions': Transaction.objects.filter(user_id=user_id)}
    return render(request,
                  'transactions/add-transactions.html',
                  context=context)


class CreateTransaction(View):
    def get(self, request):
        print('get request')
        return render(request,
                      'transactions/form.html',
                      context={'form': TransactionForm()})

    def post(self, request):
        user_id = request.user.id
        form = TransactionForm(request.POST or None)

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user_id = user_id
            transaction.save()

            context = {'transaction': transaction}
            return render(request,
                          'transactions/transaction.html',
                          context=context)






