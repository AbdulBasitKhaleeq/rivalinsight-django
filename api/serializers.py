from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'password')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBlog
        fields = '__all__'


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'

class FacebookReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookReport
        fields = '__all__'

class TwitterReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterReport
        fields = '__all__'

class WordpressReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordpressReport
        fields = '__all__'
