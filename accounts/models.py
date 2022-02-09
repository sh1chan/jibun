from django.db import models

from . import config


# TODO
#   - created_date
#   - description


class NumberAccounts(models.Model):
    """Model to store a phone number
    """
    full_number = models.CharField(max_length=config.PHONE_NUMBER_MAX_LENGTH)


class EmailAccounts(models.Model):
    """Model to store an email address
    """
    full_email = models.CharField(max_length=config.EMAIL_ADDRESS_MAX_LEGNTH)
