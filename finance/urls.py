from django.urls import path

from . import views
from .views import DashboardView, TransactionsView, add_transactions, CreateTransaction

app_name = 'finance'


urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('transactions/', TransactionsView.as_view(), name='transactions'),
    path('transactions/new/', add_transactions, name='new_transaction'),
    path('create_transaction_form/', CreateTransaction.as_view(), name='create-transaction')
]
