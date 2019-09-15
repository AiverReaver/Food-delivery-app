from django.urls import path

from .views import register, token, refresh_token, revoke_token

urlpatterns = [
    path('register/', register),
    path('token/', token),
    path('token/refresh/', refresh_token),
    path('token/revoke/', revoke_token),
]
