from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Memories(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    title = models.CharField(max_length=120,  verbose_name="Título")
    content = models.TextField(verbose_name="Conteúdo")
    unlock_date = models.DateField(verbose_name="Data de desbloqueio", null=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Memorias' # nome da tabela no banco

    def __str__(self):
        return self.title # Exibe o campo name

    def is_unlocked(self):
        return timezone.now().date() >= self.unlock_date
