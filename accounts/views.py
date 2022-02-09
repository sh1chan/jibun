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
        'phone_number_length': config.PHONE_NUMBER_MAX_LENGTH,
        'email_address_length': config.EMAIL_ADDRESS_MAX_LEGNTH,
    }
    return render(request, 'accounts/index.html', context)


@require_http_methods(['POST'])
def register_phone_number(request):
    # TODOC
    return 'hi:phone'


@require_http_methods(['POST'])
def register_email_address(request):
    # TODOC
    return 'hi:email'
