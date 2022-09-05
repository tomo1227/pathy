from django.urls import path
from .views import MyUserAPIView

urlpatterns = [
    path('detail/', MyUserAPIView.as_view()),
]