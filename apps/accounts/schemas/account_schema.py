from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        max_length=150,
        validators=[UniqueValidator(queryset=User.objects.all(),
                                    message="Este nome de usuário já está em uso.")],
        error_messages={
            'unique': "Este nome de usuário já está em uso.",
        }
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(),
                                    message="Este e-mail já está cadastrado.")],
    )  # valida obrigatoriedade e unicidade de e-mail :contentReference[oaicite:4]{index=4}
    password = serializers.CharField(write_only=True, required=True, min_length=8)  # só grava, não retorna :contentReference[oaicite:5]{index=5}

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        # create_user cuidará de hashear a senha corretamente
        return User.objects.create_user(**validated_data)



class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'
    def validate(self, attrs):
        # Executa a validação padrão e obtém o dict com 'refresh' e 'access'
        data = super().validate(attrs)

        # Adiciona dados do usuário autenticado
        data['user'] = {
            'username': self.user.username,
            'email': self.user.email,
        }

        return data
