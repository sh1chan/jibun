from .models import AccountModel


class AccountModelQuery:
    """Query functions for AccountModel
    """
    __slots__ = ()

    @staticmethod
    def get_accounts():
        return AccountModel.objects.all().order_by('id')
