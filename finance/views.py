from django.http import HttpRequest
from django.shortcuts import render
from finance.services.render.dashboard import Dashboard
from finance.services.render.transactions import TransactionsPage


def dashboard_page(request: HttpRequest):
    user_id = request.user.id
    content_render = Dashboard.get_content(user_id)
    return render(request, 'dashboard/main.html', context=content_render)


def transactions_page(request: HttpRequest):
    user_id = request.user.id
    content_render = TransactionsPage.get_content(user_id)
    return render(request, 'transactions/main.html', context=content_render)


"""def add_transaction(request: HttpRequest):
    if request.method == 'POST':
        category = request.POST.dict()

    return render(request, 'finance/forms/transaction-form.html',
                  context={'categories': categories,
                           'transaction_types': ['Income',
                                                 'Expense'],
                           'payment_methods': ['Cash',
                                               'Debit card',
                                               'Credit card'],
                           'budgets': ['budget1', 'budget2']

                           })


def add_budget(request: HttpRequest):
    if request.method == 'POST':
        category = request.POST.dict()
        print(category)

    return render(request, 'finance/forms/budget-form.html',
                  context={
                      'wallets': ['(wallet_name: amount)',
                                  '(wallet_name2: amount2)',
                                  '(wallet_name3: amount3)'],
                      'bank_accounts': ['(bank_name: amount)',
                                        '(bank_name2: amount2)',
                                        '(bank_name3: amount3)']
                  })


def add_wallets(request: HttpRequest):
    if request.method == 'POST':
        category = request.POST.dict()
        print(category)

    return render(request, 'finance/wallet-form.html')


def add_loan(request: HttpRequest):
    if request.method == 'POST':
        category = request.POST.dict()
        print(category)

    return render(request, 'finance/loan-form.html')


def add_mandatory_pay(request: HttpRequest):
    if request.method == 'POST':
        category = request.POST.dict()
        print(category)

    return render(request, 'finance/mandatory-pay-form.html')"""
