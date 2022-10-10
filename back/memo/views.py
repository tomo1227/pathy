from django.http import HttpResponse
from rest_framework import viewsets

from .models import Article
from .serializer import ArticleSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
