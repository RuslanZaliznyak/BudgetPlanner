from finance.models.wallets import Wallet, BankAccount


class WalletData:
    @classmethod
    def get_all_wallets(cls, user_id):
        try:
            result = Wallet.objects.filter(user_id=user_id)
            return result
        except Wallet.DoesNotExist:
            # If the result is None, returns an empty object
            return Wallet.objects.none()
        except Exception as e:
            print(f"Error: {e}")
            return None


class BankAccountData:
    @classmethod
    def get_all_accounts(cls, user_id):
        return BankAccount.objects.filter(user_id=user_id)


