from django.urls import path
from . import views
from rest_framework import routers
from .views import ArticleViewSet

urlpatterns = [
    path('', views.index, name='index'),
]
router = routers.DefaultRouter()
router.register('articles', ArticleViewSet)
