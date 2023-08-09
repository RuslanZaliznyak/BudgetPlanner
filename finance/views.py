from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView

from finance.forms.account import AccountForm
from finance.forms.transaction import TransactionForm
from finance.models.transaction import Transaction
from finance.services.data.account import AccountData
from finance.services.data.transaction import TransactionData


def get_account_list(request):
    return render(request, 'dashboard/account-str.html')


def add_account_to_list(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204)

    else:
        form = AccountForm
        return render(request,
                      'dashboard/account-form.html',
                      {'form': form})


class DashboardView(View):
    template_name = 'dashboard/dashboard.html'
    initial = {'key': 'value'}

    @staticmethod
    def get_content(user_id):
        return {
            'transactions': TransactionData.get_all_by_user(user_id),
            'accounts': AccountData.get_all_by_user(user_id),
            'categories': TransactionData.get_all_categories(user_id),
            'expense_categories': [1, 2, 3]
        }

    def get(self, request, *args, **kwargs):
        print(request.user.id)
        accounts = self.get_content(13).get('accounts')
        print(accounts)
        return render(request, self.template_name, {"accounts": accounts})


class TransactionsView(ListView):
    template_name = 'transactions/transactions.html'
    model = Transaction
    context_object_name = 'transactions'


# Func who renders page with transactions forms - TO REDESIGN
def add_transactions(request):
    user_id = request.user.id
    context = {'form': TransactionForm(),
               'transactions': Transaction.objects.filter(user_id=user_id).order_by('-created_at')}
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


class CreateAccount(View):
    def get(self, request):
        return render(request,
                      'dashboard/account-form.html',
                      context={'form': AccountForm()})

    def post(self, request):
        user_id = request.user.id
        form = AccountForm(request.POST or None)

        if form.is_valid():
            account = form.save(commit=False)
            account.user_id = user_id
            account.save()

            context = {'account': account}
            return render(request,
                          'dashboard/account-row.html',
                          context=context)



