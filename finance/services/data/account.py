from finance.models import Account


class AccountData:
    @classmethod
    def get_all_by_user(cls, user_id):
        try:
            accounts = Account.objects.filter(user_id=user_id)
            return accounts
        except Account.DoesNotExist:
            return Account.objects.none()
        except Exception as e:
            print(f"Error: {e}")
            return None
