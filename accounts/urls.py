from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_accounts),
    path('<int:account_id>/', views.get_account),
]
