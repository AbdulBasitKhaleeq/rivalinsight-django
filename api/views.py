from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser, IsLoggedInUser, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny




class BlogViewSet(viewsets.ModelViewSet):
    def get_queryset(self, *args, **kwargs):
        return UserBlog.objects.all().filter(user=self.request.user)
    serializer_class = BlogSerializer

    def perform_craete(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsLoggedInUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]
        return [permission() for permission in permission_classes]


class DetailViewSet(viewsets.ModelViewSet):
    def get_queryset(self, *args, **kwargs):
        return UserDetail.objects.all().filter(user=self.request.user)
    serializer_class = DetailSerializer

    def perform_craete(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsLoggedInUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]
        return [permission() for permission in permission_classes]