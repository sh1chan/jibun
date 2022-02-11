from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from . import config


@require_http_methods(['GET'])
def index(request):
    """Accounts Dashboard
    """
    context = {
        'phone_numbers': [1, 2, 3, 4, 5, 6, 7, 8],
        'email_addresses': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
        'supported_accounts': (
            ('phone_number', config.PHONE_NUMBER_MAX_LENGTH),
            ('email_address', config.EMAIL_ADDRESS_MAX_LEGNTH),
        )
    }
    return render(request, 'accounts/index.html', context)


@require_http_methods(['GET'])
def account(request, account_id: int):
    """Account Dashboard
    """
    return render(request, 'accounts/account.html')


@require_http_methods(['POST'])
def register_phone_number(request):
    # TODOC
    return 'hi:phone'


@require_http_methods(['POST'])
def register_email_address(request):
    # TODOC
    return 'hi:email'
