from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('<int:account_id>/', views.account),
]
