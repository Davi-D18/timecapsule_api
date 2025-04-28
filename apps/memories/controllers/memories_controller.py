from rest_framework.viewsets import generics

from apps.memories.schemas.memorie_schema import MemorySerializer, UnlockMemorySerializer
from apps.memories.models.memories import Memories
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from apps.memories.permissions import IsOwner


class MemoryListCreateView(generics.ListCreateAPIView):
    serializer_class = MemorySerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        # retorna só memórias do usuário
        return Memories.objects.filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):
        # Get username from request data
        username = self.request.data.get('owner')
        
        # Check if user exists in database
        try:
            user = User.objects.get(email=username)
            serializer.save(owner=user)
        except User.DoesNotExist:
            raise ValidationError({"detail": "Usuário não cadastrado"})


class MemoryDetailView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwner]

    def get_queryset(self):
        memory_id = self.kwargs['pk']
        return Memories.objects.filter(id=memory_id)

    def get_serializer_class(self):
        instance = self.get_object()

        if instance.is_unlocked():
            return UnlockMemorySerializer
        return MemorySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if not instance.is_unlocked():
            return Response(
                {
                    "detail": f"Essa memória estará disponível em: {instance.unlock_date}",
                    "title": f"{instance.title}",
                    "unlock": f"{instance.unlock_date}",
                    "created_at": f"{instance.created_at}"
                }
            )

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
