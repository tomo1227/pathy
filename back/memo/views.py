from django.shortcuts import render
from django.http import HttpResponse
import django_filters
from rest_framework import viewsets, filters

from .models import Article
from .serializer import ArticleSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
