from django.contrib import admin
from apps.memories.models.memories import Memories

@admin.register(Memories)
class MemoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'unlock_date', 'owner', 'created_at')
    search_fields = ('title', 'content', 'owner__username')
    list_filter = ('unlock_date', 'owner')
    ordering = ('id',)