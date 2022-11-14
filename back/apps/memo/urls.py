from django.urls import path
from rest_framework import routers
from apps.memo.views import ArticleViewSet, index

urlpatterns = [
    path('', index, name='index'),
]
router = routers.DefaultRouter()
router.register('articles', ArticleViewSet)
