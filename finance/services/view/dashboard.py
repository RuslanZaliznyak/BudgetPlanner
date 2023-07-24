import datetime

from finance.services.data.transaction import TransactionData
from finance.services.data.budget import BudgetData
from finance.services.data.wallets import WalletData, BankAccountData


class Dashboard:
    @classmethod
    def get_content(cls, user_id):
        return {
            'transactions': TransactionData.get_all_by_user(user_id),
            'budget': BudgetData.get_by_user(user_id)[0],
            'wallets': WalletData.get_all_wallets(user_id),
            'bank_accounts': BankAccountData.get_all_accounts(user_id),
            'budget_daily_limit': BudgetData.get_daily_limit(user_id),
            'categories': TransactionData.get_expense_activity(user_id,
                                                               start_date=datetime.datetime(2023, 1, 1),
                                                               end_date=datetime.datetime(2023, 1, 2))
        }
