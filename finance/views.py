from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

categories = [
    'Groceries',
    'Transportation',
    'Entertainment',
    'Utilities',
    'Healthcare',
    'Travel',
    'Clothing',
    'Education',
    'Housing',
    'Miscellaneous',
]


def dashboard(request: HttpRequest):
    return render(request, 'finance/dashboard/dashboard.html',
                  context={
                      'user_name': 'TEST USER',
                      'current_balance': 'BALANCE_COUNT',
                      'total_income': 'TOTAL_INCOME',
                      'total_expense': 'TOTAL_EXPENSE',
                      'cards': None,
                      'transactions': ['one', 'two', 'three'],
                  })


def add_transaction(request: HttpRequest):
    if request.method == 'POST':
        category = request.POST.dict()
        print(category)

    return render(request, 'finance/transaction-form.html',
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

    return render(request, 'finance/mandatory-pay-form.html')
