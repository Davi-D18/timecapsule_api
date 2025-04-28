from django.urls import path
from apps.memories.controllers.memories_controller import MemoryListCreateView, MemoryDetailView


urlpatterns = [
    path('memories/', MemoryListCreateView.as_view()),
    path('memories/<int:pk>/', MemoryDetailView.as_view()),
]