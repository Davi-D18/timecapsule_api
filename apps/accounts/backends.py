from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Captura o email que pode vir em 'email' ou 'username'
        email = kwargs.get('email') or username
        UserModel = get_user_model()
        try:
            # Busca usuário ignorando caixa alta/baixa
            user = UserModel.objects.get(email__iexact=email)
        except UserModel.DoesNotExist:
            return None
        # Verifica senha e flags como is_active
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
