from django.urls import path

from .views import DashboardView, TransactionsView, add_transactions, CreateTransaction, add_account_to_list, get_account_list

app_name = 'finance'


urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('transactions/', TransactionsView.as_view(), name='transactions'),
    path('transactions/new/', add_transactions, name='new_transaction'),
    path('create_transaction_form/', CreateTransaction.as_view(), name='create-transaction'),


    path('create_account_form/', add_account_to_list, name='add_account'),
    path('get-account-list', get_account_list, name='get_account_list')
]
