from django.conf import settings


def created_applications(request):
    return {
        'CREATED_APPLICATIONS': settings.CREATED_APPS,
    }
