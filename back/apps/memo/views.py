from django.http import HttpResponse
from rest_framework import viewsets#, filters

# from django_filters import rest_framework as filters
# from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter


from apps.memo.models import Article
from apps.memo.serializer import ArticleSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ("title", "article_text", "author__username")
    search_fields = (
        "$title",
        "$article_text",
        "$author__username"
    )
    ordering_fields = ("title", "created_at", "updated_at", "author__username")
