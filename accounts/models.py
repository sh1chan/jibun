from django.db import models

from . import config


# TODO
#   - created_date
#   - description


class PhoneNumberModel(models.Model):
    """Model to store a phone number
    """
    phone_number = models.CharField(max_length=config.PHONE_NUMBER_MAX_LENGTH)


class EmailAddressModel(models.Model):
    """Model to store an email address
    """
    email_address = models.CharField(max_length=config.EMAIL_ADDRESS_MAX_LEGNTH)
