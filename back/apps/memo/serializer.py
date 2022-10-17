# coding: utf-8
from rest_framework import serializers
from djoser.serializers import UserSerializer
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Article
        fields = "__all__"
