from .models import PhoneNumberModel, EmailAddressModel


class PhoneNumberQuery:
    """Query functions for NumberAccount model
    """
    __slots__ = ()

    @staticmethod
    def get_accounts():
        return PhoneNumberModel.objects.all().order_by('id')


class EmailAddressQuery:
    """Query functions for EmailAccounts model
    """
    __slots__ = ()

    @staticmethod
    def get_accounts():
        return EmailAddressModel.objects.all().order_by('id')
