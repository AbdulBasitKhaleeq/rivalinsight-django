from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBlog
        fields = '__all__'


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'
