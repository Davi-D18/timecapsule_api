from django.urls import path, include


urlpatterns = [
    path('', include('apps.memories.routes.memories_routes')),
]
