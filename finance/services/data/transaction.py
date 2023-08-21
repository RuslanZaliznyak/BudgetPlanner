import datetime

from django.db.models import Sum
from django.utils import timezone
from finance.models.transaction import Transaction, TransactionCategory
import pandas as pd


class TransactionData:
    @classmethod
    def get_all_by_user(cls, user_id):
        try:
            transactions = Transaction.objects.select_related('payment_method').filter(user_id=user_id)
            return transactions
        except Transaction.DoesNotExist:
            return Transaction.objects.none()
        except Exception as e:
            print(f"Error: {e}")
            return None

    @classmethod
    def get_all_categories(cls):
        try:
            # BUG
            result = TransactionCategory.objects.all()
            return result
        except TransactionCategory.DoesNotExist:
            return TransactionCategory.objects.none()
        except Exception as e:
            print(f"Error: {e}")
            return None

    @classmethod
    def get_by_id(cls, transaction_id):
        pass

    @classmethod
    def get_by_date(cls, user_id, search_date=None):
        if search_date is None:
            search_date = timezone.now().date()

        transactions = Transaction.objects.filter(
            user_id=user_id,
            datetime__date=search_date
        )
        return transactions

    @classmethod
    def get_for_period(cls, user_id, start_date: datetime, end_date: datetime):
        transactions = Transaction.objects.prefetch_related(
            'user_id', 'category_id', 'transaction_type_id', 'description_id', 'payment_method_id'
        ).filter(
            user_id=user_id,
            created_at__range=(start_date, end_date)
        )
        return transactions

    @classmethod
    def get_expense_activity(cls,
                             user_id,
                             start_date: datetime,
                             end_date: datetime,
                             top_n=3):

        transactions_for_period = cls.get_for_period(user_id, start_date, end_date)

        transaction_sort = transactions_for_period. \
                               values('category_id__name'). \
                               annotate(total_amount=Sum('amount')). \
                               order_by('-total_amount')[:top_n]

        df = pd.DataFrame(transaction_sort)
        df['total_amount'] = df['total_amount'].astype(int)
        total_sum = df['total_amount'].sum()
        df['percentage'] = round((df['total_amount'] / total_sum) * 100, 2)
        percentage_data = df.set_index('category_id__name').to_dict(orient='index')

        return percentage_data


