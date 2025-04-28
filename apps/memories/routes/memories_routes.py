from django.urls import path
from apps.memories.controllers.memories_controller import MemoryListCreateView, MemoryDetailView, MemoriesPublics


urlpatterns = [
    path('memories/', MemoryListCreateView.as_view()),
    path('memories/<int:pk>/', MemoryDetailView.as_view()),
    path('memories/publics/', MemoriesPublics.as_view()),
]