from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    api_registration_view,
)

app_name = 'account'

urlpatterns = [
    path('register', api_registration_view, name='api_registration'),
    path('login', obtain_auth_token, name='api_login'),
]
