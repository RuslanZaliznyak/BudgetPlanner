from finance.models.budget import Budget
from finance.services.data.transaction import TransactionData


class BudgetData:
    @classmethod
    def get_by_user(cls, user_id):
        try:
            result = Budget.objects.filter(user_id=user_id)
            return result
        except Budget.DoesNotExist:
            # If the result is None, returns an empty object
            return Budget.objects.none()
        except Exception as e:
            print(f"Error: {e}")
            return None

    @classmethod
    def count_daily_transactions(cls, user_id, search_date=None):
        daily_transactions = TransactionData.get_by_date(user_id, search_date)

        return \
            sum([float(i.amount) for i in daily_transactions if i.transaction_type_id.name == 'Expense'])

    @classmethod
    def get_daily_limit(cls, user_id):
        daily_limit = Budget.objects.filter(user_id=user_id)[0].daily_limit_amount
        total_transactions = cls.count_daily_transactions(user_id)
        exceed_percentage = int(((total_transactions - float(daily_limit)) / float(daily_limit)) * 100)

        return {
            'daily_limit': daily_limit,
            'total_transactions': total_transactions,
            'exceed_percentage': exceed_percentage
        }

