import datetime

from finance.services.data.account import AccountData
from finance.services.data.transaction import TransactionData
from finance.services.data.budget import BudgetData

"""TransactionData.get_expense_activity(
                user_id,
                datetime.datetime(2023, 7, 1),
                datetime.datetime(2023, 7, 31)"""


class Dashboard:
    @classmethod
    def get_content(cls, user_id):
        return {
            'transactions': TransactionData.get_all_by_user(user_id),
            'accounts': AccountData.get_all_by_user(user_id),
            'categories': TransactionData.get_all_categories(user_id),
            'expense_categories': [1, 2, 3]
        }
