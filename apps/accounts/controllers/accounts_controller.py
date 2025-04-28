from rest_framework import generics, permissions
from apps.accounts.schemas.account_schema import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.accounts.schemas.account_schema import EmailTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]  # qualquer um pode criar conta
    serializer_class = RegisterSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer