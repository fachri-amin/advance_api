from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    api_registration_view,
    account_properties_view,
    account_update_view
)

app_name = 'account'

urlpatterns = [
    path('login', obtain_auth_token, name='api_login'),
    path('properties', account_properties_view, name='api_account_properties'),
    path('register', api_registration_view, name='api_registration'),
    path('update', account_update_view, name='api_account_update'),
]
