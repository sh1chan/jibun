from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from . import config
from .query import AccountModelQuery


@require_http_methods(['GET'])
def get_accounts(request):
    """Accounts Dashboard
    """
    context = {
        # 'accounts': AccountModelQuery.get_accounts(),
        'accounts': [1, 2, 3, 4, 5, 6, 7],
    }
    return render(request, 'accounts/index.html', context)


@require_http_methods(['GET'])
def get_account(request, account_id: int):
    """Account Dashboard
    """
    return render(request, 'accounts/account.html')


@require_http_methods(['POST'])
def register_account(request, k):
    # TODOC
    return 'hi:phone'
