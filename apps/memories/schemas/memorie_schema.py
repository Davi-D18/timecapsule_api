from rest_framework import serializers
from apps.memories.models.memories import Memories

class MemorySerializer(serializers.ModelSerializer):
    unlock_date = serializers.DateField(required=True)
    title = serializers.CharField(required=True, max_length=120)

    class Meta:
        model = Memories
        fields = ['id', 'title', 'unlock_date', 'content', 'owner', 'created_at']
        extra_kwargs = {
            'content': {'write_only': True},
            'owner': {'read_only': True},
        }


class UnlockMemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memories
        fields = ['id', 'title', 'unlock_date', 'content', 'created_at']
        extra_kwargs = {
            'owner': {'write_only': True},
        }