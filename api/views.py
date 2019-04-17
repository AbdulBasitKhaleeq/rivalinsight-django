from django.shortcuts import render
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser, IsLoggedInUser, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser)

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

class FacebookReportViewSet(viewsets.ModelViewSet):
    def get_queryset(self, *args, **kwargs):
        return FacebookReport.objects.all().filter(user=self.request.user)
    serializer_class = FacebookReportSerializer

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

class TwitterReportViewSet(viewsets.ModelViewSet):
    def get_queryset(self, *args, **kwargs):
        return TwitterReport.objects.all().filter(user=self.request.user)
    serializer_class = TwitterReportSerializer

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

class WordpressReportViewSet(viewsets.ModelViewSet):
    def get_queryset(self, *args, **kwargs):
        return WordpressReport.objects.all().filter(user=self.request.user)
    serializer_class = WordpressReportSerializer

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


############ ------------------ Trending and Competitors

class FacebookTrendingViewSet(viewsets.ModelViewSet):
    def get_queryset(self, *args, **kwargs):
        return FacebookTrending.objects.all().filter(user=self.request.user)
    serializer_class = FacebookTrendingSerializer

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


class TwitterTrendingViewSet(viewsets.ModelViewSet):
    def get_queryset(self, *args, **kwargs):
        return TwitterTrending.objects.all().filter(user=self.request.user)
    serializer_class = TwitterTrendingSerializer

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


class TumblrTrendingViewSet(viewsets.ModelViewSet):
    def get_queryset(self, *args, **kwargs):
        return TumblrTrending.objects.all().filter(user=self.request.user)
    serializer_class = TumblrTrendingSerializer

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

class NewsTrendingViewSet(viewsets.ModelViewSet):
    def get_queryset(self, *args, **kwargs):
        return NewsTrending.objects.all().filter(user=self.request.user)
    serializer_class = NewsTrendingSerializer

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