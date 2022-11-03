from django.urls import path
from apps.memo import views
from rest_framework import routers
from apps.memo.serializer import ArticleViewSet

urlpatterns = [
    path('', views.index, name='index'),
]
router = routers.DefaultRouter()
router.register('articles', ArticleViewSet)
