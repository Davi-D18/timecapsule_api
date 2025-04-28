from django.urls import path
from apps.accounts.controllers.accounts_controller import RegisterView, EmailTokenObtainPairView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('accounts/register', csrf_exempt(RegisterView.as_view())),
    path('accounts/login', EmailTokenObtainPairView.as_view())
]