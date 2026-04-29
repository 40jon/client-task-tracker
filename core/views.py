from rest_framework import generics
from .models import Client, Task
from .serializers import ClientSerializer, TaskSerializer


class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all().order_by('-created_at')
    serializer_class = ClientSerializer
    search_fields = ['name', 'email', 'company']
    ordering_fields = ['created_at', 'name', 'company']


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    filterset_fields = ['status', 'client']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date', 'status']


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
