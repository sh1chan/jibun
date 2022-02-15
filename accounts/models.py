from django.db import models

from . import config


class AccountModel(models.Model):
    """Model for default or universal accounts
    """
    name = models.CharField(max_length=config.ACCOUNT_MODEL_NAME_LENGTH)
    description = models.TextField()
    name_type = models.CharField(max_length=config.ACCOUNT_MODEL_TYPE_LENGTH)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
