from finance.services.data.transaction import TransactionData


class TransactionsPage:
    @classmethod
    def get_content(cls, user_id):
        return {
            'transactions': TransactionData.get_all_by_user(user_id)
        }
